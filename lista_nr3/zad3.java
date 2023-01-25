import java.security.SecureRandom;

public class RandomPassword {
    private static final String CHAR_LOWER = "abcdefghijklmnopqrstuvwxyz";
    private static final String CHAR_UPPER = CHAR_LOWER.toUpperCase();
    private static final String NUMBER = "0123456789";
    private static final String SPECIAL_CHAR = "!@#$%^&*_=+-/";
    private static final String PASSWORD_ALLOW_BASE = CHAR_LOWER + CHAR_UPPER + NUMBER + SPECIAL_CHAR;
    private static final int PASSWORD_LENGTH = 8;
    private static SecureRandom random = new SecureRandom();
    
    public static void main(String[] args) {
        String password = generateRandomPassword();
        System.out.println(password);
    }
    
    private static String generateRandomPassword() {
        StringBuilder password = new StringBuilder();
        for (int i = 0; i < PASSWORD_LENGTH; i++) {
            int randomCharAt = random.nextInt(PASSWORD_ALLOW_BASE.length());
            char randomChar = PASSWORD_ALLOW_BASE.charAt(randomCharAt);
            password.append(randomChar);
        }
        return new String(password);
    }
}