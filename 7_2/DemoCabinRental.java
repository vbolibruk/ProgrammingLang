// Create an abstract class named Book. Include a String field for the book’s title
// and a double field for the book’s price. Within the class, include a constructor
// that requires the book title, and add two get methods—one that returns the title
// and one that returns the price. Include an abstract method named setPrice().
// Create two child classes of Book: Fiction and NonFiction. Each must include a
// setPrice() method that sets the price for all Fiction Books to $24.99 and for
// all NonFiction Books to $37.99. Write a constructor for each subclass, and
// include a call to setPrice() within each. Write an application demonstrating
// that you can create both a Fiction and a NonFiction Book and display their
// fields. Save the files as Book.java, Fiction.java, NonFiction.java, and
// UseBook.java.

class CabinRental {
    private int cabinNumber;
    protected double rentalRate;

    CabinRental( int cabinNumber ) {
        this.cabinNumber = cabinNumber;
        if(( cabinNumber >= 1) && (cabinNumber <= 3))
            rentalRate = 950.0;
        else
            rentalRate = 1100.0;

    }

    public int get_cabinNumber() {
        return cabinNumber;
    }

    public double get_rentalRate() {
        return rentalRate;
    }

    public void printInfo() {
        System.out.println("Cabin number: " + cabinNumber +
                           "\nRental rate: " + rentalRate);
    }
}

class HolidayCabinRental extends CabinRental {

    HolidayCabinRental(int cabinNumber) {
        super(cabinNumber);
        rentalRate += 150.0;
    }

    public void printInfo() {
        System.out.println("Cabin number: " + get_cabinNumber() +
                           "\nHoliday rental rate: " + rentalRate);
    }
}

class DemoCabinRental {

    public static void main(String[] args) {

        CabinRental c1 = new CabinRental(3);
        CabinRental c2 = new CabinRental(10);

        c1.printInfo();
        c2.printInfo();

        System.out.println("Rental rate in c2 is " +
            c2.get_rentalRate());

        HolidayCabinRental c3 = new HolidayCabinRental(3);
        HolidayCabinRental c4 = new HolidayCabinRental(10);

        System.out.println("");
        c3.printInfo();
        c4.printInfo();

        System.out.println("Holiday rental rate in c4 is " +
            c4.get_rentalRate());
    }
}
