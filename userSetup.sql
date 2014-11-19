--Create Read Only Acct in SQL
GRANT SELECT ON 'beer' TO 'beer_reader'@'localhost' IDENTIFIED BY 'beer_reader';;

--Create Write Acct in SQL **BE SURE TO CHANGE THIS PASSWORD**
GRANT UPDATE,DELETE,SELECT,INSERT, ON 'beer' TO 'beer_reader'@'localhost' IDENTIFIED BY 'beer_writer';;