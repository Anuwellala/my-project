#include <stdio.h>
int main()
{
    char letter;

    printf("Enter a letter:");
    scanf("%c", &letter);

    if((letter>='a' &&letter<='z')||(letter>='A' &&letter<='Z'))
    {
        printf("This character is an alphabet");
    }
    else
    {
        printf("This character is not an alphabet");
    }

    return 0;
}
