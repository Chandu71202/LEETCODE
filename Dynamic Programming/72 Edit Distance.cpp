class Solution {
public:
    int minDistance(string word1, string word2) 
    {
        int m=word1.length();
        int n=word2.length();
        int dp[n+1][m+1];
        for(int i=0;i<=n;i++)
        {
            for(int j=0;j<=m;j++)
            {
                if(i==0)
                    dp[i][j]=j;
                else if(j==0)
                    dp[i][j]=i;
                else
                {
                if(word2[i-1]==word1[j-1])
                    dp[i][j]=dp[i-1][j-1];
                else
                    dp[i][j]=1+min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1]));
                }

             }
        }
        return dp[n][m];
    }
};
