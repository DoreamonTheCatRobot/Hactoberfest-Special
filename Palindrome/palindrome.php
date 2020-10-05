<?php 
function oneDigit($num) 
{  
	return (($num >= 0) && 
			($num < 10)); 
} 

function isPalUtil($num, $dupNum) 
{ 
	if (oneDigit($num)) 
		return ($num == ($dupNum) % 10); 
	if (!isPalUtil((int)($num / 10), 
						$dupNum)) 
		return -1; 
	$dupNum = (int)($dupNum / 10); 
  
	return ($num % 10 == ($dupNum) % 10); 
} 

function isPal($num) 
{ 

	if ($num < 0) 
	$num = (-$num); 

	$dupNum = ($num);

	return isPalUtil($num, $dupNum); 
} 

$n = 12321; 
if(isPal($n) == 0) 
	echo "Yes\n"; 
else
	echo "No\n"; 

$n = 12; 
if(isPal($n) == 0) 
	echo "Yes\n"; 
else
	echo "No\n"; 

$n = 88; 
if(isPal($n) == 1) 
	echo "Yes\n"; 
else
	echo "No\n"; 

$n = 8999; 
if(isPal($n) == 0) 
	echo "Yes\n"; 
else
	echo "No\n";
