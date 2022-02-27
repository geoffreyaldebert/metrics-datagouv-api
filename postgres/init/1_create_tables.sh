psql -U $POSTGRES_USER -d $POSTGRES_DB -c "CREATE TABLE datasets
(
	id_table SERIAL PRIMARY KEY NOT NULL,
    date CHARACTER VARYING,
    idsite CHARACTER VARYING,
    type CHARACTER VARYING,
    category CHARACTER VARYING,
    slug CHARACTER VARYING,
    id CHARACTER VARYING,
    uniq_views DECIMAL(9,2),
    views DECIMAL(9,2),
    organization_id CHARACTER VARYING
)
TABLESPACE pg_default;"

psql -U $POSTGRES_USER -d $POSTGRES_DB -c "CREATE TABLE resources
(
	id_table SERIAL PRIMARY KEY NOT NULL,
    date CHARACTER VARYING,
    idsite CHARACTER VARYING,
    type CHARACTER VARYING,
    category CHARACTER VARYING,
    id CHARACTER VARYING,
    title CHARACTER VARYING,
    dataset_id CHARACTER VARYING,
    uniq_views DECIMAL(9,2),
    views DECIMAL(9,2),
    organization_id CHARACTER VARYING
)
TABLESPACE pg_default;"

psql -U $POSTGRES_USER -d $POSTGRES_DB -c "CREATE TABLE organizations
(
	id_table SERIAL PRIMARY KEY NOT NULL,
    date CHARACTER VARYING,
    idsite CHARACTER VARYING,
    type CHARACTER VARYING,
    category CHARACTER VARYING,
    slug CHARACTER VARYING,
    id CHARACTER VARYING,
    uniq_views DECIMAL(9,2),
    views DECIMAL(9,2)
)
TABLESPACE pg_default;"