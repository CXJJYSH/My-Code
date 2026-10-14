// 温哲睿 2024201410 

public class Circle extends Point {
    private double radius;

    // 构造方法1：默认值
    public Circle() {
        super();
        this.radius = 2;
        this.color = "Blue";
    }

    // 构造方法2：指定坐标和半径
    public Circle(double x, double y, double radius) {
        super(x, y);
        this.radius = radius;
        this.color = "Blue";
    }

    // 判断点与圆的位置关系
    public void relation(Point p) {

        double d = Math.sqrt(
                Math.pow(this.x - p.x, 2)
                        + Math.pow(this.y - p.y, 2));

        if (d < radius) {
            System.out.println("Point is inside the circle.");
        } else if (d == radius) {
            System.out.println("Point is on the circle.");
        } else {
            System.out.println("Point is outside the circle.");
        }
    }

    @Override
    public void draw() {
        System.out.println(
                "Draw Circle -> Center:("
                        + x + "," + y
                        + ") Radius:"
                        + radius
                        + " Color:"
                        + color);
    }
}