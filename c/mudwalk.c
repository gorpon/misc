#include<stdio.h>
#include<string.h>

/*this simple little program has but one purpose in mind: converting mud directions from the following format:
"3n2s4u" (three north two south four up)
to the following format suitable for use with the "speedwalk" command used in dibrova muds.
(shoutz out to GodSmith, Konerak, BaldBull, and everyone else at mud.thwap.net and accessirc.net!)
"nnnssuuuu" (that's all)
to use, compile, and type: ./<executable name> <directions>

written by Gorpon, cosmic druid from beyond, level 34 and slacking.

revision history
0.1	original 2/5/04
0.11    with reverse mudwalk 2/7/04
0.111	cleaned up code a little and documented more verbosely 2/8/04
*/

char ENTSTR[255]; /*original string to be parsed from cmd args*/
char NEWSTR[4000]; /*resulting string built based on parsing arguments*/
char TMPSTR[4000]; /* for reversed string */
char C; /*current character to be processed*/
int D=0; /*digit counter.  keeps track of how many digits are in the queue. determines multiples of directions */

int POS=0; /* current position on ENTSTR we are at.  not a "P.O.S."! */
int NPOS=0; /*current position writing to NEWSTR we are at*/
int X=0; /*  a throwaway integer used for localized counting in the functions */ 
int REVERSE=0; /* new feature as of 0.11 reverse flag allows for directions to outputted in reverse format */


int strintadec() {
	/*must convert the character type to an integer, so convert the character to a string, then to an int
	explanation of variables:
	*/
	char TEMPSTR[1]; /*local var to hold character value for conversion*/
	int E; /*we shall use this as the integer value of the newly converted digit*/
	TEMPSTR[0]=C;
	E=atoi(TEMPSTR);
	/*printf("%d\n",E);*/
	return E;
}


int numbers(){
	int F;/*using F to receive str to int value for current digit position*/
	F=strintadec();

	if ( D > 0 ) /*shift the ten's place to make way for the next digit in the series*/
		D = ( D * 10 + F );
	else D = F; /*or if first digit, assign digit that value*/
}


int directions(){
	/*directions takes individual direction characters and adds them to the end of the new string. */
	if ( D > 0 ) {
		/*the following loop deals with directional characters that have been preceded by digits.
		It adds D amount of directional characters of the type discovered */
		for ( X=1; X<=D; X++ ){ 
				
			NEWSTR[NPOS]=C;
			NPOS++;
		}
		D=0;
	}
	
	/*the "else" is for a lone character without a preceding digit*/
	else {
		NEWSTR[NPOS]=C;
		NPOS++;
	}
}


print_usage() {
	printf("mudwalk version 0.11 pat@snarg.com\n");
	printf("usage: mudwalk <directions>\n");
	printf("\n");
	printf("for example this command:\n");
	printf(">mudwalk 3n2s5u\n");
	printf("\n");
	printf("should return the following output:\n");
	printf(">mudwalk 3n2s5u\n");
	printf("nnnssuuuuu\n");
	printf(">mudwalk -r 3n2s5u will reverse the output:\n");
	printf(">reversed dddddnnsss\n");
}

reverse() {
	/* reverse does two things:
	1. reverse the stream of characters
	2. reverse each character to it's directional opposite.
	This obviously won't work for asymetrical mud paths, but there's
	not much we can do about that :P
	*/
	int POS1=0; /*position in stream of string of directions 
	that have already been through the numbers() function */
	int STRLENGTH=0; /*length of the string. */
	char P; /* individual character to process */
	char T; /* reversed character */
	STRLENGTH=strlen(NEWSTR); /*get string length*/
	for ( POS1=STRLENGTH; POS1 > 0; POS1-- ) /*create a loop starting at the end of the string and go backwards*/
		{
		switch (NEWSTR[POS1-1]) { /* reverse each directional character using a switch */
	           case 'n':
	                T='s';
	                break;
	           case 's':
	                T='n';
	                break;
	           case 'w':
	                T='e';
	                break;
	           case 'e':
	                T='w';
	                break;
	           case 'u':
	                T='d';
	                break;
	           case 'd':
	                T='u';
	                break;
	           default: /* reset the character to null to avoid any possibility of unwanted characters */
	                T='\0';
	                break;
			}
		TMPSTR[STRLENGTH-POS1] = T; /*assign newly reversed direction to the end of the reversed string */
	
		}

}


int main(int argc, char *argv[]){
	
	/*print usuage information if user does not enter any arguments after the command*/
	if ( argc < 2 )
		{
		print_usage();
		}
	
	/*if "-r" is found on the first argument, the reverse flag is set*/
	else {
	if ( (strcmp(argv[1],"-r")) == 0 ) {
		strcpy(ENTSTR, argv[2]);
		REVERSE=1;
		}
	
	/*standard directional parsing if everything else fails*/
	else {	
		strcpy(ENTSTR, argv[1]);
	}
	
	/*main parsing loop.  here characters are singled out that match our criteria for digits or directions*/
	while( ENTSTR[POS] ){
		C=ENTSTR[POS];
		if ((C >= '0') && (C <= '9')) {
			numbers();
			}
		if ((C == 'n') || (C == 's') || (C == 'w') || (C == 'e') || (C == 'u') || (C == 'd')) {
			directions();
			}
		POS++;
	
	}
	
	/*after completing parsing operations, determine whether reverse mode is being requested, if not, print out
	directions and exit */
	/*printf("converted string is\n%s\n\n",NEWSTR);*/
	if ( REVERSE == 1 ) {
		reverse();
		printf("reversed %s\n", TMPSTR);
	}
	else {
		printf("%s\n",NEWSTR);
	}
	
	}
	return 0;
}
