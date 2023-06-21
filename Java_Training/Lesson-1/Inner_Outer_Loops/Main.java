public class Main {
  public static void main(String[] args) {
    // Outer loop.
    for (int i = 1; i <= 29; i++) {
      System.out.println("Outer: " + i); // Executes 2 times
      
      // Inner loop
      for (int j = 1; j <= 38; j++) {
        System.out.println(" Inner: " + j); // Executes 6 times (2 * 3)
      }
    } 
  }
}
