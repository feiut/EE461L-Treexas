package test;

import static org.junit.Assert.*;

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class SeleniumTestCases {
	private static WebDriver driver;
	@BeforeClass
	public static void makeDriver() {
		System.setProperty("webdriver.chrome.driver", "./lib/chromedriver/chromedriver.exe");
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS);
	}

	@Test
	public void mainPage() {//test 3 working links
		driver.get("http://www.treexas.com/");
		driver.findElement(By.xpath("//a[@id=\"plantlist\"]")).click();
		assertEquals(driver.getCurrentUrl(),"http://www.treexas.com/plant_list/");
		driver.navigate().back();
		assertEquals(driver.getCurrentUrl(),"http://www.treexas.com/");
		driver.findElement(By.xpath("//a[@id=\"ecoregions\"]")).click();
		assertEquals(driver.getCurrentUrl(),"http://www.treexas.com/eco_list/");
		driver.navigate().back();
		assertEquals(driver.getCurrentUrl(),"http://www.treexas.com/");
		driver.findElement(By.xpath("//a[@id=\"stateparks\"]")).click();
		assertEquals(driver.getCurrentUrl(),"http://www.treexas.com/park_list/");
		driver.navigate().back();
		assertEquals(driver.getCurrentUrl(),"http://www.treexas.com/");
	}
	@Test 
	public void plantPage() {
		driver.get("http://www.treexas.com/plant_list/");
		int size = driver.findElements(By.xpath("//a")).size();
		for(int i = 0;i<size;i++) {
			WebElement e = driver.findElements(By.xpath("//a")).get(i);
			String href = e.getAttribute("href");
			e.click();
			assertEquals(driver.getCurrentUrl(),href);
			driver.navigate().back();
		}
	}
	@Test
	public void ecoregionsPage() {
		driver.get("http://www.treexas.com/eco_list/");
		int size = driver.findElements(By.xpath("//a")).size();
		for(int i = 0;i<size;i++) {
			WebElement e = driver.findElements(By.xpath("//a")).get(i);
			String href = e.getAttribute("href");
			e.click();
			assertEquals(driver.getCurrentUrl(),href);
			driver.navigate().back();
		}
		
	}
	@Test
	public void stateparksPage() {
		driver.get("http://www.treexas.com/park_list/");
		int size = driver.findElements(By.xpath("//a")).size();
		for(int i = 0;i<size;i++) {
			WebElement e = driver.findElements(By.xpath("//a")).get(i);
			String href = e.getAttribute("href");
			e.click();
			assertEquals(driver.getCurrentUrl(),href);
			driver.navigate().back();
		}
	}
	@AfterClass
	public static void tearDown() {
		driver.quit();
	}

}
