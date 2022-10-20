const webDriver = require('selenium-webdriver');
const driver = new webDriver.Builder().forBrowser('firefox').build();
const By = webDriver.By;

const test = async () => {
    await driver.get('https://google.com');
    const searchField = driver.findElement(By.xpath('//input[@title="Search"]'));
    searchField.sendKeys('SELENIUM');
    await driver.sleep(10000);
    searchField.sendKeys(webDriver.Key.ENTER);
    await driver.sleep(10000);
    driver.close();
};

test()



