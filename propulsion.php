
<?php 
//boat propulsion backend. this responds to buttons in the UI for the control of the boat's overall movements
//gus mueller, august 23 2019
//////////////////////////////////////////////////////////////
 
 
//ini_set('display_errors', 1);
//ini_set('display_startup_errors', 1);
//error_reporting(E_ALL);


$command = "kill";


if($_REQUEST && $_REQUEST["command"]) {
	$command = $_REQUEST["command"];


 
	if($command=="kill") {
		$linuxCommand = escapeshellcmd('sudo python boatkill.py');
		passthru($linuxCommand);
		echo '{"message":"boat killed"}';
		exit;
	} else if($command=="left") { 
		$linuxCommand = escapeshellcmd('sudo python boatleft.py');
		passthru($linuxCommand);
		echo '{"message":"boat turned left"}';
		exit;
	} else if($command=="right") { 
		$linuxCommand = escapeshellcmd('sudo python boatright.py');
		passthru($linuxCommand);
		echo '{"message":"boat turned right"}';
		exit;
	} else if($command=="go") { 
		$linuxCommand = escapeshellcmd('sudo python boatpow.py');
		passthru($linuxCommand);
		echo '{"message":"boat going"}';
		exit;
	} else if($command=="rev") { 
		$linuxCommand = escapeshellcmd('sudo python boatrev.py');
		passthru($linuxCommand);
		echo '{"message":"boat backing up"}';
		exit;
	}
}
