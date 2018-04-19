#include "msrc.h"

// Add and return
int add(int a,int b)
{
    return a + b;
}

// Add and store in ref
void add(int a,int b,int* result)
{
    *result = a + b;
}