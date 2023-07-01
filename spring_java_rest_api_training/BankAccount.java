public class BankAccount {
    public static void main(String[] args) {
        double balance = 1000.75;
        double amountToWithdraw = 250;

        double updatedBalance = balance - amountToWithdraw;
        double amountForEachFriend = updatedBalance / 3;

        boolean canPurchaseTicket = amountForEachFriend >= 250;
        System.out.println("Updated balance: " + updatedBalance);
        System.out.println("Amount for each friend: " + amountForEachFriend);
        System.out.println("Can purchase ticket: " + canPurchaseTicket);
    }
}