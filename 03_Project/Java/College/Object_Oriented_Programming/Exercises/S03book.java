public class S03book {
    public static void main(String[] args) {
        Book book1 = new Book("Java编程思想", 108.0, 5);
        Book book2 = new Book("算法导论", 128.0, 3);
        Book book3 = new Book("数据结构", 89.0, 7);

        System.out.println("=== 初始图书数量 ===");
        book1.display();
        book2.display();
        book3.display();

        System.out.println("\n=== 图书借阅/归还操作 ===");
        book1.borrow();
        book2.borrow();
        book3.restore();
        book3.borrow();
        book2.borrow();
        book2.borrow();
        book1.restore();
        book1.display();
    }

    static class Book {
        private String bookname;
        private double price;
        private int number;

        public Book(String bookname, double price, int number) {
            this.bookname = bookname;
            this.price = price;
            this.number = number;
        }

        public void display() {
            System.out.println("书名：" + bookname +
                    "，价格：" + price +
                    "，存书数量：" + number);
        }

        public void borrow() {
            if (number > 0) {
                number--;
                System.out.println("【借书成功】《" + bookname + "》，剩余：" + number);
            } else {
                System.out.println("【借书失败】《" + bookname + "》库存不足！");
            }
        }

        public void restore() {
            number++;
            System.out.println("【还书成功】《" + bookname + "》，库存：" + number);
        }
    }
}

// 2026.05.29 11:34