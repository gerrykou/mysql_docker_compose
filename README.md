# MySQL Workbench & MySQL with docker-compose

```shell
docker-compose up
docker exec -it db-mysql bash
```
    mysql -u root -proot

        create database mydatabase;
        use mydatabase;

        create table employees (
            id int not null,
            name text,
            primary key (id)
        );

        insert into employees (id, name) values (1, 'George');
        insert into employees (id, name) values (2, 'Georgio'), (3, 'Nick');

```shell
docker-compose -f workbench.docker-compose.yaml up
docker-compose -f workbench.docker-compose.yaml down
```
-- In the connection settings, `Hostname` should be `db-mysql` as the service is named on the [workbench.docker-compose.yaml](workbench.docker-compose.yaml#L18) file
