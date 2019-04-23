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
import org.openqa.selenium.Keys;
import org.openqa.selenium.Point;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

public class SeleniumTestCases {
	private static WebDriver driver;
	private static WebDriverWait wait;
	@BeforeClass
	public static void makeDriver() {
		System.setProperty("webdriver.chrome.driver", "./lib/chromedriver/chromedriver.exe");
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS);
		wait = new WebDriverWait(driver, 10);
	}

	@Test
	public void mainPage() {//test main page
		driver.get("http://www.treexas.com/");
		driver.findElement(By.xpath("//*[@id=\"mainpage\"]/div[2]/nav/div/div[2]/ul/li[1]/a")).click();
		assertEquals("http://www.treexas.com/plant_list/",driver.getCurrentUrl());
		driver.navigate().back();
		assertEquals(driver.getCurrentUrl(),"http://www.treexas.com/");
		driver.findElement(By.xpath("//*[@id=\"mainpage\"]/div[2]/nav/div/div[2]/ul/li[3]/a")).click();
		assertEquals("http://www.treexas.com/eco_list/",driver.getCurrentUrl());
		driver.navigate().back();
		assertEquals("http://www.treexas.com/",driver.getCurrentUrl());
		driver.findElement(By.xpath("//*[@id=\"mainpage\"]/div[2]/nav/div/div[2]/ul/li[2]/a")).click();
		assertEquals("http://www.treexas.com/park_list/",driver.getCurrentUrl());
		driver.navigate().back();
		driver.findElement(By.xpath("//*[@id=\"mainpage\"]/div[2]/nav/div/div[2]/ul/li[4]/a")).click();
		assertEquals("http://www.treexas.com/about/",driver.getCurrentUrl());
		driver.navigate().back();
		assertEquals("http://www.treexas.com/",driver.getCurrentUrl());
	}
	@Test 
	public void plantPage() {
		driver.get("http://www.treexas.com/plant_list/");
		int i = 1;
		while(i<54) {
			i++;
			List<WebElement> e1 = new ArrayList<WebElement>();
			e1 = driver.findElements(By.xpath("//*[@id=\"page_footer\"]/ul/li"));
			int s=e1.size();
			e1.get(s-3).click();
			assertEquals("http://www.treexas.com/plant_list/?page="+i,driver.getCurrentUrl());
		}
		
		/*int size = driver.findElements(By.xpath("/html/body/div[2]/div")).size();
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
		}*/
	}
	@Test
	public void ecoregionsPage() {
		driver.get("http://www.treexas.com/eco_list/");
		int size = driver.findElements(By.xpath("/html/body/div/div[2]/div/map/area")).size();
		assertEquals(14,size);
		for(int i = 0;i<size;i++) {
			WebElement e = driver.findElements(By.xpath("/html/body/div/div[2]/div/map/area")).get(i);
			String href = e.getAttribute("href");
			driver.get(href);
			assertEquals(href,driver.getCurrentUrl());
			driver.navigate().back();
		}
		
	}
	@Test
	public void stateparksPage() {
		driver.get("http://www.treexas.com/park_list/");
		driver.findElement(By.xpath("//*[@id=\"page_footer\"]/ul/li[7]/a"));
		int i = 1;
		while(i<8) {
			i++;
			List<WebElement> e1 = new ArrayList<WebElement>();
			e1 = driver.findElements(By.xpath("//*[@id=\"page_footer\"]/ul/li"));
			int s=e1.size();
			e1.get(s-3).click();
			assertEquals("http://www.treexas.com/park_list/?page="+i,driver.getCurrentUrl());
		}
		/*int size = driver.findElements(By.xpath("/html/body/div/div[3]/div")).size();
		for(int i = 0;i<size;i++) {
			WebElement e = driver.findElements(By.xpath("/html/body/div/div[3]/div")).get(i);
			String href = e.findElement(By.cssSelector("a")).getAttribute("href");
			e.click();
			List<WebElement> e1 = new ArrayList<WebElement>();
			e1=driver.findElements(By.xpath("/html/body/div[1]/div[2]/div/h1"));
			assertNotEquals("State Park id: "+i,0,e1.size());
			assertEquals(href,driver.getCurrentUrl());
			driver.navigate().back();
		}*/
	}
	@Test
	public void searchMain() {//switches toggle and finds a state park
		driver.get("http://www.treexas.com/");
		WebElement toggle = driver.findElement(By.xpath("//*[@id=\"search_bar\"]/div[1]/select"));
		WebElement in=driver.findElement(By.xpath("//*[@id=\"search_bar\"]/input"));
		WebElement but = driver.findElement(By.xpath("//*[@id=\"search_bar\"]/div[2]/button"));
		Select dropdown = new Select(toggle);
		dropdown.selectByIndex(1);
		in.sendKeys("Abilene State Park");
		but.click();
		List<WebElement> e1 = new ArrayList<WebElement>();
		e1 = driver.findElements(By.xpath("/html/body/div/div[3]/div/a"));
		assertNotEquals(0,e1.size());
		assertEquals("http://www.treexas.com/park_profile/?id=0",e1.get(0).getAttribute("href"));
	}
	@Test
	public void searchParks() {
		driver.get("http://www.treexas.com/park_list/");
		WebElement in=driver.findElement(By.xpath("//*[@id=\"search_bar\"]/input"));
		WebElement but = driver.findElement(By.xpath("//*[@id=\"search_bar\"]/div/button"));
		in.sendKeys("atlanta");
		but.click();
		List<WebElement> e1 = new ArrayList<WebElement>();
		e1 = driver.findElements(By.xpath("/html/body/div/div[3]/div/a"));
		assertNotEquals(0,e1.size());
		assertEquals("http://www.treexas.com/park_profile/?id=1",e1.get(0).getAttribute("href"));
	}
	@Test
	public void searchPlants() {
		driver.get("http://www.treexas.com/plant_list/");
		List<WebElement> e1 = new ArrayList<WebElement>();
		e1 = driver.findElements(By.xpath("//*[@id=\"filters\"]/form/div/select"));
		int i=0;
		for(WebElement e: e1) {
			if(i<e1.size()-2) {
				Select dropdown = new Select(e);
				dropdown.selectByIndex(1);
			}
			i++;
		}
		wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"filters\"]/form/div/button")));
		driver.findElement(By.xpath("//*[@id=\"filters\"]/form/div/button")).sendKeys(Keys.RETURN);
		e1 = driver.findElements(By.xpath("//*[@id=\"plantlist\"]/div/div[1]/a"));
		assertNotEquals(0,e1.size());
		assertEquals("http://www.treexas.com/plant_profile/?id=4",e1.get(0).getAttribute("href"));
	}
	@AfterClass
	public static void tearDown() {
		driver.quit();
	}

}
