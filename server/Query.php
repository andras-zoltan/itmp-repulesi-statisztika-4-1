<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Query
 *
 * @author Huri Gábor
 */
class Query {
    public $db;
    public function __construct() {
        include_once 'Database.php';
        $this->db = new Database();
    }
    
    public function toroltJaratokAranya($legitarsasag){
        $lekerdezes = "SELECT SUM(arr_cancelled)/SUM(arr_flights)*100 FROM flight "
                . "WHERE carrierid = :l";
        $select = $this->db->prepare($lekerdezes);
        $select->bindParam(":l", $legitarsasag);
        if($select->execute()){
            return sprintf("%.1f", $select->fetch()[0]);
        }
        else {
            print "Hiba<br>";
            print "<pre>";
            print_r($select->errorInfo());
            print "</pre>";
            return -1;
        }
    }
    
    public function osszesJarat($legitarsasag){
        $lekerdezes = "SELECT SUM(arr_flights) FROM flight "
                . "WHERE carrierid = :l";
        $select = $this->db->prepare($lekerdezes);
        $select->bindParam(":l", $legitarsasag);
        if($select->execute()){
            return $select->fetch()[0];
        }
        else {
            print "Hiba<br>";
            print "<pre>";
            print_r($select->errorInfo());
            print "</pre>";
            return -1;
        }
    }
    
    public function legitarsasagokNevei(){
        $lekerdezes = "SELECT id, name FROM carrier ORDER BY name";
        $select = $this->db->prepare($lekerdezes);
        if($select->execute()){
            return $select->fetchAll();
        }
        else {
            print "Hiba<br>";
            print "<pre>";
            print_r($select->errorInfo());
            print "</pre>";
        }
    }
}

