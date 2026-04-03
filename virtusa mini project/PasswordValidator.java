import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class PasswordValidator {

    public static void main(String[] args){
        Scanner inputScanner = new Scanner(System.in);
        boolean isPasswordSecure = false;

        System.out.println("=== SafeLog Employee Portal ===");
        System.out.println("Your password must contain: At least 8 characters, 1 uppercase letter, and 1 digit.");


        while (!isPasswordSecure){
            System.out.print("\nEnter your new password: ");
            String userInput = inputScanner.nextLine();

            List<String> validationFeedback = analyzePassword(userInput);

            if(validationFeedback.isEmpty()){
                System.out.println("Success! Password meets all corporate security policies.");
                isPasswordSecure = true;
            }else{
                System.out.println("Password Invalid. Please fix the following issues:");
                for (String error : validationFeedback){
                    System.out.println("   - " + error);
                }
            }
        }
        inputScanner.close();
    }

    private static List<String> analyzePassword(String password) {
        List<String> errorMessages = new ArrayList<>();


        if (password.length() < 8) {
            errorMessages.add("Too short (must be at least 8 characters).");
        }

        boolean foundUppercase = false;
        boolean foundDigit = false;


        for (int i = 0; i < password.length(); i++) {
            char currentChar = password.charAt(i);

            if (Character.isUpperCase(currentChar)) {
                foundUppercase = true;
            }
            if (Character.isDigit(currentChar)) {
                foundDigit = true;
            }
        }

        if (!foundUppercase) {
            errorMessages.add("Missing an uppercase letter.");
        }
        if (!foundDigit) {
            errorMessages.add("Missing a digit (0-9).");
        }

        return errorMessages;
    }
}
