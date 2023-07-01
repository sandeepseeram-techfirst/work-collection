public class GreaterLessThan {
    public static void main(String[] args) {
        double creditsEarned = 176.5;
        double creditsOfSeminar = 8;
        double creditsToGraduate = 180;

        double creditsAfterSeminar = creditsEarned + creditsOfSeminar;
        System.out.println("Credits earned after seminar: " + creditsAfterSeminar);
        System.out.println("Credits to graduate is less than credits after seminar? " + (creditsToGraduate < creditsAfterSeminar));
    }
}