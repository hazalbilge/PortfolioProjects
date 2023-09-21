/* 
Cleaning Data in SQL Queries
*/
select *
from public."nashvillehousing"

--Standardize date format
select SaleDate, convert(SaleDate, date)
from public."nashvillehousing"
Update public."nashvillehousing"
SET SaleDate = convert(SaleDate, date)

Alter table public."nashvillehousing"
Add SaleDateConverted date;

Update public."nashvillehousing"
SET SaleDate = convert(SaleDate, date)
-------------------------------------------------------------
--Populate property address data
select *
from public."nashvillehousing"
--where PropertyAddress is null
order by ParceLID

select a.ParceLID, a.PropertyAddress, b.ParceLID, b.propertyaddress,COALESCE(b.propertyaddress,a.PropertyAddress)
from "nashvillehousing" a
JOIN "nashvillehousing" b
on a.ParceLID = b.ParceLID
 AND a.UniqueID <> b.UniqueID
--where a.PropertyAddress is null

Update "nashvillehousing" 
SET PropertyAddress = COALESCE(a.propertyaddress,b.PropertyAddress)
from "nashvillehousing" a
JOIN "nashvillehousing" b
on a.ParceLID = b.ParceLID
 AND a.UniqueID <> b.UniqueID
---------------------------------------------------------------------
--Breaking out adress into individuals columns (adress,city,state)
select PropertyAddress
from public."nashvillehousing"
--where PropertyAddress is null
--order by ParceLID

SELECT 
SUBSTRING(PropertyAddress, 1, POSITION(',' IN PropertyAddress)-1) AS address,
POSITION(',' IN PropertyAddress)
FROM public."nashvillehousing";
--Alternate sql code because of -1 gives error for postgresql
SELECT 
  CASE 
    WHEN POSITION(',' IN PropertyAddress) > 0 
    THEN SUBSTRING(PropertyAddress, 1, POSITION(',' IN PropertyAddress) - 1) 
    ELSE PropertyAddress 
  END AS address,
  SUBSTRING(PropertyAddress,POSITION(',' IN PropertyAddress)+1,length(PropertyAddress)) as ad,
  POSITION(',' IN PropertyAddress) AS comma_position
FROM public."nashvillehousing";
-- we add address and city as diff columns
Alter table public."nashvillehousing"
Add PropertySplitAddress char(255);

Update public."nashvillehousing"
SET PropertySplitAddress =  CASE 
    WHEN POSITION(',' IN PropertyAddress) > 0 
    THEN SUBSTRING(PropertyAddress, 1, POSITION(',' IN PropertyAddress) - 1) 
    ELSE PropertyAddress 
  END 

Alter table public."nashvillehousing"
Add PropertySplitCity char(255);

Update public."nashvillehousing"
SET PropertySplitCity =   SUBSTRING(PropertyAddress,POSITION(',' IN PropertyAddress)+1,length(PropertyAddress)) 

select *
from public."nashvillehousing"
select
split_part(replace(OwnerAddress, ',', '.'), '.', 1) as Adress,
split_part(replace(OwnerAddress, ',', '.'), '.', 2) as City,
split_part(replace(OwnerAddress, ',', '.'), '.', 3) as ParseState
from public."nashvillehousing"

Alter table public."nashvillehousing"
Add OwnerSplitAddress char(255);

Update public."nashvillehousing"
SET OwnerSplitAddress =  split_part(replace(OwnerAddress, ',', '.'), '.', 1)

Alter table public."nashvillehousing"
Add OwnerSplitCity char(255);

Update public."nashvillehousing"
SET OwnerSplitCity = split_part(replace(OwnerAddress, ',', '.'), '.', 2)  
-----------------------------------------------------------------
-- Change Y and N to Yes and No in "Sold as Vacant" field
select distinct(SoldAsVacant), count(SoldAsVacant)
from public."nashvillehousing"
group by SoldAsVacant
order by 2


select SoldAsVacant,
CASE WHEN SoldAsVacant='Y' THEN 'Yes'
 WHEN SoldAsVacant='N' THEN 'No' 
 ELSE SoldAsVacant
 END
from public."nashvillehousing"
Update public."nashvillehousing"
SET SoldAsVacant =  CASE WHEN SoldAsVacant='Y' THEN 'Yes'
 WHEN SoldAsVacant='N' THEN 'No' 
 ELSE SoldAsVacant
 END

-------------------------------------------------------------------
-- Remove Duplicates
WITH RowNumCTE AS(
select *,
ROW_NUMBER() OVER(
	PARTITION BY ParceLID,
				 PropertyAddress,
				 SalePrice,
				 SaleDate,
				 LegalReference
                 ORDER BY 
                     UniqueID) row_num
from public."nashvillehousing"
--order by ParceLID
)
delete
from RowNumCTE
WHERE row_num>1

select *
from RowNumCTE
--order by PropertyAddress

----------------------------------------------------
-- Delete Unused Columns
select *
from public."nashvillehousing"

alter table public."nashvillehousing"
drop column OwnerAddress, 
drop column TaxDistrict,
drop column  PropertyAddress

alter table public."nashvillehousing"
drop column SaleDate


