for year in {20..21} ; 
do 
    for month in {01..12}; 
    do 

        psql -U $POSTGRES_USER -d $POSTGRES_DB -c "COPY datasets(date, idsite, type, category, slug,id, uniq_views, views, organization_id) FROM '/tmp/consolidated_datasets/piwik_20${year}_${month}.csv' delimiter ',' CSV HEADER ENCODING 'UTF8';"

        psql -U $POSTGRES_USER -d $POSTGRES_DB -c "COPY resources(date, idsite, type, category, id, title, dataset_id, uniq_views, views, organization_id) FROM '/tmp/consolidated_resources/piwik_20${year}_${month}.csv' delimiter ',' CSV HEADER ENCODING 'UTF8';"

        psql -U $POSTGRES_USER -d $POSTGRES_DB -c "COPY organizations(date, idsite, type, category, slug,id, uniq_views, views) FROM '/tmp/consolidated_organizations/piwik_20${year}_${month}.csv' delimiter ',' CSV HEADER ENCODING 'UTF8';"
    done;
done;


psql -U $POSTGRES_USER -d $POSTGRES_DB -c "COPY datasets(date, idsite, type, category, slug,id, uniq_views, views, organization_id) FROM '/tmp/consolidated_datasets/piwik_2022_01.csv' delimiter ',' CSV HEADER ENCODING 'UTF8';"

psql -U $POSTGRES_USER -d $POSTGRES_DB -c "COPY resources(date, idsite, type, category, id, title, dataset_id, uniq_views, views, organization_id) FROM '/tmp/consolidated_resources/piwik_2022_01.csv' delimiter ',' CSV HEADER ENCODING 'UTF8';"

psql -U $POSTGRES_USER -d $POSTGRES_DB -c "COPY organizations(date, idsite, type, category, slug,id, uniq_views, views) FROM '/tmp/consolidated_organizations/piwik_2022_01.csv' delimiter ',' CSV HEADER ENCODING 'UTF8';"




psql -U $POSTGRES_USER -d $POSTGRES_DB -c "COPY datasets(date, idsite, type, category, slug,id, uniq_views, views, organization_id) FROM '/tmp/consolidated_datasets/piwik_2022_02.csv' delimiter ',' CSV HEADER ENCODING 'UTF8';"

psql -U $POSTGRES_USER -d $POSTGRES_DB -c "COPY resources(date, idsite, type, category, id, title, dataset_id, uniq_views, views, organization_id) FROM '/tmp/consolidated_resources/piwik_2022_02.csv' delimiter ',' CSV HEADER ENCODING 'UTF8';"

psql -U $POSTGRES_USER -d $POSTGRES_DB -c "COPY organizations(date, idsite, type, category, slug,id, uniq_views, views) FROM '/tmp/consolidated_organizations/piwik_2022_02.csv' delimiter ',' CSV HEADER ENCODING 'UTF8';"