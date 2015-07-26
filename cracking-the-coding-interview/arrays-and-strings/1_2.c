void reverse(char *s) {
    if (s){
        char tmp;
        char *end = s;

        while(*end){
            end++;
        }
        end--;
        while(s < end) {
            tmp = *s;
            *s = *end;
            *end = tmp;
            s++;
            end--;
        }
    }
}

void main() {
    char s[] = "sharad";
    reverse(s);
    printf("%s\n",s);
}