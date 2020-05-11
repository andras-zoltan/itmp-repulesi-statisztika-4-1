<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Database
 *
 * @author Huri Gábor
 */
class Database extends PDO{
    public function __construct(){
        parent::__construct("mysql:host=localhost;dbname=id13655741_jaratok;charset=utf8", "id13655741_americanflights", "OmZ6]hYHttIbC@E");
    }
}
