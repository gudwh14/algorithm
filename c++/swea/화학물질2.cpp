#include<stdio.h>
 
int t, n, arr[100][100],cache[20][20],check[101],mat[101],m[21],mcnt,front,rear;
#define Min(A,B) ((A)>(B)?(B):(A))
 
int main()
{
    scanf("%d", &t);
    for (int test = 1; test <= t; test++,mcnt=0)
    {
        printf("#%d ", test);
        scanf("%d", &n);
        for (int i = 0; i < n; i++)for (int j = 0; j < n; j++)scanf("%d", &arr[i][j]);
        for (int i = 0; i < n; i++)for (int j = 0; j < n; j++)
        {
            if (arr[i][j])
            {
                int row, col;
                for (int ii = i;; ii++)
                {
                    if (!arr[ii][j])
                    {
                        col = ii - i;
                        check[row]++;
                        check[col]--;
                        mat[row] = col;
                        break;
                    }
                    for (int jj = j;; jj++)
                    {
                        if (!arr[ii][jj])
                        {
                            row = jj - j;
                            break;
                        }
                        arr[ii][jj] = 0;
                    }
                }
            }
        }
        for (int i = 1; i < 101; i++)
        {
            if (check[i] == 1)front = i;
            if (check[i] == -1)rear = i;
            check[i] = 0;
        }
        m[mcnt++] = front;
        while (1)
        {
            if (front == rear)break;
            front = mat[front];
            m[mcnt++] = front;
        }
        
        for (int L = 1; L < mcnt; L++)
        {
            for (int i = 1; i <= mcnt - L; i++)
            {
                int k = i + L;
                cache[i][k] = 987654321;
                for (int j = i; j < k; j++)
                {
                    cache[i][k] = Min(cache[i][k], cache[i][j] + cache[j + 1][k] + m[i - 1] * m[k] * m[j]);
                }
            }
        }
        printf("%d\n", cache[1][mcnt - 1]);
    }
}
