<?php

function toUpper($str) {
    $new_str = "";
    foreach(str_split($st) as $chr) {
        $new_str = $new_str . strtoupper($str);
    }
    return $new_str;
}

class FindInvitationsTest extends \PHPUnit_Framework_TestCase 
{
    public function testToUpper()
    {
        $this->assertEquals(toUpper('Hello World'), 'HELLO WORLD');
    }
}

