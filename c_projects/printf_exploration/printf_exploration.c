// Import the standard input-output (I/O) header file for the printf() function.
// The printf() function outputs objects in string format to the standard output device, such as the terminal.
# include <stdio.h>

// Define the main method as an integer to eventually return zero to end the programme.
int main() {
    // ========== The printf() Function and Newlines ==========

    // The printf() function does not generate newlines by default. Add \n to do this.
    printf("Welcome to Matirgo's C-based simple projects folder!\n");
    printf("Let's learn C together!\n");

    // ========== Format Specifiers ==========

    // Topic print statement to make the final terminal output prettier.
    printf("\n===== Format Specifiers =====\n\n");

    // Format specifiers are used in the printf() function to tell the compiler the type of data a variable stores.
    // They start with percentage signs (%) followed by an alphabetic character dependent on the data type.
    // "%d" and "%i" is for type int, "%c" for type char, "%f" or "%F" for type float, "%s" is for type string, and "%lf" is for type double.

    // Define different variables of different types.
    int exampleInteger = 10;
    float exampleFloat = 4.2;
    char exampleChar = 'M'; // NOTE! Use single quotes for defining char type variables! Can also assign ASCII values.

    // Utilise format specifiers to print the contents of the variables.
    printf("%d\n", exampleInteger); // printf(exampleInteger) will not work.
    printf("%f\n", exampleFloat); // printf(exampleFloat) will not work.
    printf("%c\n", exampleChar); // printf(exampleChar) will not work.
    
    // Putting it all together, and adding in a hard-coded value.
    printf("You are a %d out of %d, %f is the best number but %d is more popular, and my name begins with %c.\n", exampleInteger, exampleInteger, exampleFloat, 7, 77);
    
    return 0;
}