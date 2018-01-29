Date 10/10/2017

***********************************************************************************
Name-:Sagar Vinayak Badhe
Roll no: 16102
Sub-Syspro
contact:8390563979
email-:sagarbadhe95@gmail.com 
***************************************************/

File folder contains:
macro_def_generate.py=> to generate the output
macro.asm => input file in this file i write some macroes

*******************************************************************************************
What is this ?
-------------	

	This is the programme files to create MNT(macro name table) & MDT(macro defination table)
In this progrmmes i write code to store the information of macroes from tha asssembly code.
and after that when assembly programme excute that time when macro call is occured then defination of this
macro replace by our tables.
****************************************************************************************

How to use this programmes files ?
----------------------------------


1)After run the following command to execute the code
	
	$ python macro_def_generate.py

This command create the required output files that is 'macro_op.txt'
and allmcro call get replaced by the defination

2)To see the result use following command
	

	i)To see the output of the programme execute following command.
	
		$cat macro_op.txt



