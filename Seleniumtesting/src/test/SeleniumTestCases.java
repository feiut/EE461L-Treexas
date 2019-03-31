package test;

import static org.junit.Assert.*;

import java.util.ArrayList;
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
import org.openqa.selenium.support.ui.WebDriverWait;

public class SeleniumTestCases {
	private static WebDriver driver;
	@BeforeClass
	public static void makeDriver() {
		System.setProperty("webdriver.chrome.driver", "./lib/chromedriver/chromedriver.exe");
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS);
		WebDriverWait wait = new WebDriverWait(driver, 10);
	}

	@Test
	public void mainPage() {//test 3 working links
		driver.get("http://www.treexas.com/");
		try {
			TimeUnit.SECONDS.sleep(10);
		} catch (InterruptedException e2) {
			e2.printStackTrace();
		}
		driver.findElement(By.xpath("/html/body/nav/div/div[2]/ul/li[1]/a")).click();
		assertEquals("http://www.treexas.com/plant_list/",driver.getCurrentUrl());
		driver.navigate().back();
		assertEquals(driver.getCurrentUrl(),"http://www.treexas.com/");
		driver.findElement(By.xpath("/html/body/nav/div/div[2]/ul/li[3]/a")).click();
		assertEquals("http://www.treexas.com/eco_list/",driver.getCurrentUrl());
		driver.navigate().back();
		assertEquals("http://www.treexas.com/",driver.getCurrentUrl());
		driver.findElement(By.xpath("/html/body/nav/div/div[2]/ul/li[2]/a")).click();
		assertEquals("http://www.treexas.com/park_list/",driver.getCurrentUrl());
		driver.navigate().back();
		assertEquals("http://www.treexas.com/",driver.getCurrentUrl());
	}
	@Test 
	public void plantPage() {
		driver.get("http://www.treexas.com/plant_list/");
		try {
			TimeUnit.SECONDS.sleep(10);
		} catch (InterruptedException e2) {
			e2.printStackTrace();
		}
		int size = driver.findElements(By.xpath("/html/body/div[2]/div")).size();
		assertEquals(806,size);
		for(int i = 0;i<size;i++) {
			WebElement e = driver.findElements(By.xpath("/html/body/div[2]/div")).get(i);
			String href = e.findElement(By.cssSelector("a")).getAttribute("href");
			e.click();
			List<WebElement> e1 = new ArrayList<WebElement>();
			e1=driver.findElements(By.xpath("//*[@id=\"plant_fields\"]/div/font[1]"));
			assertEquals(driver.getCurrentUrl(),href);
			assertNotEquals(0,e1.size());
			driver.navigate().back();
		}
	}
	@Test
	public void ecoregionsPage() {
		driver.get("http://www.treexas.com/eco_list/");
		try {
			TimeUnit.SECONDS.sleep(10);
		} catch (InterruptedException e2) {
			e2.printStackTrace();
		}
		int size = driver.findElements(By.xpath("/html/body/div/div[2]/div[2]/map/area")).size();
		assertEquals(15,size);
		for(int i = 0;i<size;i++) {
			WebElement e = driver.findElements(By.xpath("/html/body/div/div[2]/div[2]/map/area")).get(i);
			String href = e.getAttribute("href");
			driver.get(href);
			List<WebElement> e1 = new ArrayList<WebElement>();
			e1=driver.findElements(By.xpath("/html/body/div/div[2]/div/h1"));
			assertNotEquals(0,e1.size());
			assertEquals(href,driver.getCurrentUrl());
			driver.navigate().back();
		}
		
	}
	@Test
	public void stateparksPage() {
		driver.get("http://www.treexas.com/park_list/");
		try {
			TimeUnit.SECONDS.sleep(10);
		} catch (InterruptedException e2) {
			e2.printStackTrace();
		}
		int size = driver.findElements(By.xpath("/html/body/div/div[3]/div")).size();
		for(int i = 0;i<size;i++) {
			WebElement e = driver.findElements(By.xpath("/html/body/div/div[3]/div")).get(i);
			String href = e.findElement(By.cssSelector("a")).getAttribute("href");
			e.click();
			List<WebElement> e1 = new ArrayList<WebElement>();
			e1=driver.findElements(By.xpath("/html/body/div[1]/div[2]/div/h1"));
			assertNotEquals(0,e1.size());
			assertEquals(href,driver.getCurrentUrl());
			driver.navigate().back();
		}
	}
	@Test
	public void search() {
		driver.get("http://www.treexas.com/");
		WebElement in=driver.findElement(By.xpath("/html/body/div/form/div/input"));
		WebElement but = driver.findElement(By.xpath("/html/body/div/form/div/div/button"));
		in.sendKeys("ABELIA, CONFETTI");
		but.click();
		List<WebElement> e1 = new ArrayList<WebElement>();
		e1 = driver.findElements(By.xpath("/html/body/div[2]/div/a"));
		assertNotEquals(0,e1.size());
		assertEquals("http://www.treexas.com/plant_profile/?id=0",e1.get(0).getAttribute("href"));
	}
	@AfterClass
	public static void tearDown() {
		driver.quit();
	}

}
