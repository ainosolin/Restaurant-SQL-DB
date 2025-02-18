<!-- PROJECT LOGO -->
<br />
<p align="center">
  </a>

  <h3 align="center">Restaurant SQL database</h3>

  <p align="center">
    A small database project for Basics of database systems-course.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Creation of database begins with collecting necessary requirements. The business case is to create database for a restaurant chain. Following requirements are set for the database:

* allow the restaurant company to display their menu with different price for meals,
* show their working hours in the week, and
* save information of all orders from their customers.

Conceptual ER-model based on the requirements:

![Conceptual ER Model](https://github.com/ainosolin/Restaurant-SQL-DB/blob/master/Files/Conceptual.png?raw=true)

The schema and database are created in MySQL Workbench after which Python is used to insert data into the tables. Data is generated using Mockaroo and stored as CSV-files, which are read into pandas dataframes and finally inserted into SQL tables.

### Built With

* [Python IDLE](https://docs.python.org/3/library/idle.html)
* [MySQL Workbench](https://www.mysql.com/products/workbench/)
* [Mockaroo](https://www.mockaroo.com/)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

[Aino Solin](https://www.linkedin.com/in/ainosolin/)
