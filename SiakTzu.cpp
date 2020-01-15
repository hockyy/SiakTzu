//new.cpp
/*
Author : Hocky Yudhiono
06-Aug-19 12:40:08 PM
Current Local Time : 12:40:08

Coded in Windows 10 Home
ASUS G550JX

getchar_unlocked > getchar > cin without sync > scanf > cin with sync
bool operator<(const MyStruct& rhs) const

On how to print Long Double to 5 decimal places :
printf("%.5Lf",ans);

On how to get random numbers :
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count()); //For int
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count()); //For LL
cout << rng() << endl;
shuffle(isi.begin(),isi.end(),rng);

__gcd(a,b)
__builtin_ffs(a) first on bit
__builtin_clz(a) count leading zero
__builtin_ctz(a) count trailing zero
__builtin_popcount(a) numbers of on bits

*/

//#include <unordered_map>
//#include <unordered_set>

//#include <random>
//#include <chrono>

//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <limits>
#include <string>
#include <vector>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>

//using namespace __gnu_pbds;
using namespace std;

#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC optimize(3)
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC target("sse3","sse2","sse")
#pragma GCC target("avx","sse4","sse4.1","sse4.2","ssse3")
#pragma GCC target("f16c")
#pragma GCC optimize("inline","fast-math","unroll-loops","no-stack-protector")
// #pragma GCC diagnostic error "-fwhole-program"
// #pragma GCC diagnostic error "-fcse-skip-blocks"
// #pragma GCC diagnostic error "-funsafe-loop-optimizations"
// #pragma GCC diagnostic error "-std=c++14"
// #pragma GCC target ("string"...)
#pragma GCC push_options
#pragma GCC pop_options
#pragma GCC reset_options
#pragma GCC optimize ("O3")

typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef pair<long long,long long> PLL;
// typedef tree<long long, null_type, less<long long>, rb_tree_tag, tree_order_statistics_node_update> pbds;
//If the time limit is strict, try not to use long double


#define fbo find_by_order
#define ook order_of_key
#define popf pop_front
#define pf push_front
#define popb pop_back
#define mp make_pair
#define pb push_back
#define remove erase
#define fi first
#define se second

//Remember to undefine if the problem is interactive
#define endl '\n'
#define DEBUG(X) cout << ">>> DEBUG(" << __LINE__ << ") " << #X << " = " << (X) << endl

const double eps = 1e-9;
const int INFMEM = 63;
const int INF = 1061109567;
const LL LINF = 4557430888798830399LL;
const double DINF = numeric_limits<double>::infinity();
const LL MOD = 1000000007;
const int dx[8] = {1,0,-1,0,1,1,-1,-1};
const int dy[8] = {0,1,0,-1,1,-1,1,-1};
const double PI = 3.141592653589793;

#ifdef _WIN32
#define getchar_unlocked getchar
#endif
#define GETCHAR getchar_unlocked
inline void fastll(LL &input_number) 
{
    input_number = 0;
    int ch = GETCHAR();
    int sign = 1;
    while(ch < '0' || ch > '9'){
        if(ch == '-') sign=-1;
        ch = GETCHAR();
    }
    while(ch >= '0' && ch <= '9'){
        input_number = (input_number << 3)+(input_number << 1) + ch-'0';
        ch = GETCHAR();
    }
    input_number *= sign;
}

inline void open(string a){
    freopen((a+".in").c_str(),"r",stdin);
    freopen((a+".out").c_str(),"w",stdout);
}

inline void fasterios(){
    //Do not use if interactive
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
} 

int main(){
    cout << "var matkul_code = [";
    LL cnt = 0;
	while(++cnt){
    	string s;
		cin >> s;
		if(s == "-1") break;	
		if(cnt != 1) cout << ",";
		cout << "\"" << s << "\"";
    }
    cout << "]" << endl;
    return 0;
}
