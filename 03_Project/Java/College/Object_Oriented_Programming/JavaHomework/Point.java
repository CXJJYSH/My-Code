// 温哲睿 2024201410 

public class Point implements Draw {
    protected double x;
    protected double y;
    protected String color;

    // 构造方法1：默认坐标[1,1]，红色
    public Point() {
        this.x = 1;
        this.y = 1;
        this.color = "Red";
    }

    // 构造方法2：指定坐标，红色
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
        this.color = "Red";
    }

    // 计算与另一点之间的距离
    public double distance(Point p) {
        double d = Math.sqrt(
                Math.pow(this.x - p.x, 2)
                        + Math.pow(this.y - p.y, 2));

        System.out.println("Distance = " + d);
        return d;
    }

    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public void draw() {
        System.out.println(
                "Draw Point -> Position:("
                        + x + "," + y + ") Color:"
                        + color);
    }
}