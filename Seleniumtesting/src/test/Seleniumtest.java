package test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Seleniumtest {
	
	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver", "./lib/chromedriver/chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.get("http://www.treexas.com/");
		driver.manage().window().maximize();
		driver.findElement(By.xpath("//a[@id=\"plantlist\"]")).click();
		
		driver.findElement(By.xpath("//a[@id=\"ecoregions\"]")).click();
		driver.findElement(By.xpath("//a[@id=\"stateparks\"]")).click();
		
		//driver.quit();
		//*[@id="plantlist"]
	}
}
