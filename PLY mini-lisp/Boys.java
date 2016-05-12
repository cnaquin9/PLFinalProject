import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by Carley on 5/10/2016.
 */
public class Boys {
    private String name;
    private int age;
    private String type;
    private String height;
    private String eyeColor;
    private String major;

    public Boys(String name, int age, String type, String height, String eyeColor, String major) {
        this.name = name;
        this.age = age;
        this.type = type;
        this.height = height;
        this.eyeColor = eyeColor;
        this.major = major;

    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getAge() {
        return age;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public String getHeight() {
        return height;
    }

    public void setEyeColor(String eyeColor) {
        this.eyeColor = eyeColor;
    }

    public String getEyeColor() {
        return eyeColor;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public String getMajor() {
        return major;
    }

}