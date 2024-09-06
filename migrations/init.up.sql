CREATE TABLE vectors
(
    id         serial primary key not null,
    vector     FLOAT8[] not null,
    text       TEXT               not null,
    created_at TIMESTAMP(6) WITHOUT TIME ZONE NOT NULL DEFAULT transaction_timestamp()
);