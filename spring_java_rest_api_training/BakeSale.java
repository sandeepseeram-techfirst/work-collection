public class BakeSale {
    public static void main(String[] args) {
        int numCookies = 17;

        // Customer buys 3 cookies
        numCookies -= 3;

        // Another customer buys half of the remaining cookies
        numCookies /= 2;

        System.out.println(numCookies);
    }
} 