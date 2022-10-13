# MySQL Workbench & MySQL with docker-compose

## Run MySQL Workbench & MySQL with docker-compose
```shell
docker-compose -f workbench.docker-compose.yaml up
docker-compose -f workbench.docker-compose.yaml down
```
-- In the connection settings, `Hostname` should be `db-mysql`  
as the service is named on the [workbench.docker-compose.yaml](workbench.docker-compose.yaml#L18) file

To Access MySQL Workbench go to http://localhost:3001/

## Run MySQL with docker-compose
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

# Extract MySql table to .csv with Python

```shell
python3 -m virtualenv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

Create a file named `pipeline.conf`:
```
[mysql_config]  
hostname = localhost  
port = 3306  
username = root  
database = mydatabase  
password = root
```
