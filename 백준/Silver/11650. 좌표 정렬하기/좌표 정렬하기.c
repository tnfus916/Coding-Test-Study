#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
typedef struct data {
	int x;
	int y;
}data;
 
int comp(const void* a, const void* b) {
	struct data* ptra = (struct data*)a;
	struct data* ptrb = (struct data*)b;
 
	if (ptra->x < ptrb->x) return -1;
	else if (ptra->x == ptrb->x) {
		if (ptra->y < ptrb->y) return -1;
		else if (ptra->y > ptrb->y) return 1;
	}
	else return 1;
}
 
int main() {
	struct data a[100000];
	int n;
	scanf("%d\n",&n);
	for(int i=0;i<n;i++){
		scanf("%d %d\n",&a[i].x,&a[i].y);
	}
	qsort((int*)a, (size_t)n, sizeof(data), comp);
	for(int i=0;i<n;i++){
		printf("%d %d\n",a[i].x,a[i].y);
	}
}