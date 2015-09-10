#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void reverse(char *str){
    char *end = str;
    char tmp;

    if (str) {
        while (*end){
            ++end;
        }

    --end;

    while (str < end){
        tmp = *str;
        *str++ = *end;
        *end-- = tmp;
        }
    }
}

void main() {
    char s[] = "sharad";
    reverse(s);
    printf("%s\n",s);
}
