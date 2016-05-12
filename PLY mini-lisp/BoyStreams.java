import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BoyStreams{
    public static void runBoys() {

        ArrayList<Boys> potentialLoveInterests = new ArrayList<>();
        Boy b1 = new Boy("Tyler", 20, "Funny", "6'0", "Green", "Engineer");
        Boy b2 = new Boy("Evan", 23, "Stupid", "5'11", "Brown", "Communications");
        Boy b3 = new Boy("Steven", 19, "Smart", "6'2", "Blue", "Computer Science");
        Boy b4 = new Boy("Aaron", 21, "Boring", "6'1", "Hazel", "Economics");
        Boy b5 = new Boy("Cody", 20, "Stupid", "5'9", "Blue", "Pre-law");
        boy.add(b1); boy.add(b2); boys.add(b3); boys.add(b4); boys.add(b5);

        System.out.println("Select * from potentialLoveInterests: \n");
        potentialLoveInterests.stream()
                .forEach(e -> {
                    System.out.println(Arrays.asList(e.getName() + ", " + e.getAge() + ", " + e.getType() + ", " + e.getHeight() + ", " + e.getEyeColor() + ", " + e.getMajor()));
                });

        System.out.println("\n\nSelect name, age, type, major from potentialLoveInterests: \n");
        potentialLoveInterests.stream()
                .forEach(e -> {
                    System.out.print(Arrays.asList(e.getName() + ", " + e.getAge() + ", " + e.getType() + ", " + e.getMajor()) + "\n");
                });

        System.out.println("\n\nSelect name, age, type, major where age > 20: \n");
        potentialLoveInterests.stream()
                .filter(e ->
                        e.getAge() > 20)
                .forEach(e -> {
                    System.out.print(Arrays.asList(e.getName() + ", " + e.getAge() + ", " + e.getType() + ", " + e.getMajor()) + "\n");
                });

        System.out.println("\n\nSelect name, age, type, major where age > 20, sort by name: \n");
        potentialLoveInterests.stream()
                .filter(e ->
                        e.getAge() > 20)
                .sorted((e, e1) -> (e.getName().compareTo(e1.getName())))
                .map(e -> Arrays.asList(e.getName() + ", " + e.getAge() + ", " + e.getType() + ", " + e.getMajor()) + "\n")
                .forEach(e -> {
                    System.out.print(e);
                });


        System.out.println("\n\nSelect name, age, type, major where age > 20, sort by age desc: \n");
        potentialLoveInterests.stream()
                .filter(e ->
                        e.getAge() > 20)
                .sorted((e, e1) -> Integer.compare(e1.getAge(), e.getAge()))
                .map(e -> Arrays.asList(e.getName() + ", " + e.getAge() + ", " + e.getType() + ", " + e.getMajor()) + "\n")
                .forEach(e -> {
                    System.out.print(e);
                });


    }

}