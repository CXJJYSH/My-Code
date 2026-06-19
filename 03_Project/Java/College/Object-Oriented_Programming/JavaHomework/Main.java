public class Main {
    public static void main(String[] args) {

        // 1. 实例化一个红色点，一个蓝色圆
        Point p = new Point(3, 4);

        Circle c = new Circle(1, 1, 5);

        // 2. 计算点与圆心距离（调用Point的方法）
        System.out.println("Distance between point and circle center:");
        p.distance(c);

        // 3. 判断点与圆的位置关系（调用Circle的方法）
        System.out.println("Position relation:");
        c.relation(p);

        // 4. 画绿色点和黄色圆
        p.setColor("Green");
        c.setColor("Yellow");

        System.out.println("Drawing:");
        p.draw();
        c.draw();
    }
}