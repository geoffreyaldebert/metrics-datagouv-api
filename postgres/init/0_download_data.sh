su - $POSTGRES_USER
mkdir -p /tmp/consolidated_datasets
mkdir -p /tmp/consolidated_resources
mkdir -p /tmp/consolidated_organizations

for year in {20..21} ; 
do 
    for month in {01..12}; 
    do 
        cd /tmp/consolidated_datasets && wget https://object.files.data.gouv.fr/opendata/datagouv/dashboard/consolidated_datasets/piwik_20${year}_${month}.csv
        cd /tmp/consolidated_resources && wget https://object.files.data.gouv.fr/opendata/datagouv/dashboard/consolidated_resources/piwik_20${year}_${month}.csv
        cd /tmp/consolidated_organizations && wget https://object.files.data.gouv.fr/opendata/datagouv/dashboard/consolidated_organizations/piwik_20${year}_${month}.csv
        done;
done;

cd /tmp/consolidated_datasets && wget https://object.files.data.gouv.fr/opendata/datagouv/dashboard/consolidated_datasets/piwik_2022_01.csv
cd /tmp/consolidated_resources && wget https://object.files.data.gouv.fr/opendata/datagouv/dashboard/consolidated_resources/piwik_2022_01.csv
cd /tmp/consolidated_organizations && wget https://object.files.data.gouv.fr/opendata/datagouv/dashboard/consolidated_organizations/piwik_2022_01.csv

cd /tmp/consolidated_datasets && wget https://object.files.data.gouv.fr/opendata/datagouv/dashboard/consolidated_datasets/piwik_2022_02.csv
cd /tmp/consolidated_resources && wget https://object.files.data.gouv.fr/opendata/datagouv/dashboard/consolidated_resources/piwik_2022_02.csv
cd /tmp/consolidated_organizations && wget https://object.files.data.gouv.fr/opendata/datagouv/dashboard/consolidated_organizations/piwik_2022_02.csv
