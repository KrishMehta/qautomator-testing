const { remote } = require('webdriverio');

async function testCase1(client) {
    try {
        // Verify the splash screen displays correctly upon launching the app.
        const splashScreen = await client.$('//XCUIElementTypeStaticText[contains(@label, "Introducing Hotels on ixigo")]');
        if (await splashScreen.isDisplayed()) {
            console.log('Splash screen displayed correctly.');
        } else {
            throw new Error('Splash screen not displayed.');
        }
    } catch (error) {
        console.error('Error in testCase1:', error);
        throw error;
    }
}

async function testCase2(client) {
    try {
        // Verify navigation to the main screen after the splash screen.
        await client.pause(3000); // Wait for splash screen transition
        const mainScreen = await client.$('//XCUIElementTypeStaticText[contains(@label, "Flights")]');
        if (await mainScreen.isDisplayed()) {
            console.log('Navigated to the main screen successfully.');
        } else {
            throw new Error('Main screen not displayed.');
        }
    } catch (error) {
        console.error('Error in testCase2:', error);
        throw error;
    }
}

async function testCase3(client) {
    try {
        // Verify the flight search interface is displayed after selecting "Flights."
        const flightsButton = await client.$('//XCUIElementTypeStaticText[contains(@label, "Flights")]');
        await flightsButton.click();
        const flightSearchInterface = await client.$('//XCUIElementTypeStaticText[contains(@label, "Search Flights")]');
        if (await flightSearchInterface.isDisplayed()) {
            console.log('Flight search interface displayed.');
        } else {
            throw new Error('Flight search interface not displayed.');
        }
    } catch (error) {
        console.error('Error in testCase3:', error);
        throw error;
    }
}

async function testCase4(client) {
    try {
        // Verify the user can enter flight search details.
        await client.$('//XCUIElementTypeTextField[@name="Departure"]')
            .setValue('IAD');
        await client.$('//XCUIElementTypeTextField[@name="Arrival"]')
            .setValue('ZRH');
        console.log('Flight search details entered successfully.');
    } catch (error) {
        console.error('Error in testCase4:', error);
        throw error;
    }
}

async function testCase5(client) {
    try {
        // Verify the "Search Flights" button functionality.
        const searchFlightsButton = await client.$('//XCUIElementTypeButton[contains(@label, "Search Flights")]');
        await searchFlightsButton.click();
        const loadingAnimation = await client.$('//XCUIElementTypeActivityIndicator');
        if (await loadingAnimation.isDisplayed()) {
            console.log('Loading animation displayed.');
        } else {
            throw new Error('Loading animation not displayed.');
        }
    } catch (error) {
        console.error('Error in testCase5:', error);
        throw error;
    }
}

async function testCase6(client) {
    try {
        // Verify the "Flight Status" screen displays correctly after searching for flights.
        await client.pause(5000); // Wait for loading to complete
        const flightStatusScreen = await client.$('//XCUIElementTypeStaticText[contains(@label, "Flight Status")]');
        if (await flightStatusScreen.isDisplayed()) {
            console.log('Flight Status screen displayed.');
        } else {
            throw new Error('Flight Status screen not displayed.');
        }
    } catch (error) {
        console.error('Error in testCase6:', error);
        throw error;
    }
}

async function testCase7(client) {
    try {
        // Verify the user can search for scheduled flights by entering an airport.
        const searchBar = await client.$('//XCUIElementTypeTextField[contains(@label, "Search scheduled airport")]');
        await searchBar.setValue('Charlottesville (CHO)');
        console.log('Airport searched successfully.');
    } catch (error) {
        console.error('Error in testCase7:', error);
        throw error;
    }
}

async function testCase8(client) {
    try {
        // Verify the user can view departure flights.
        const departuresTab = await client.$('//XCUIElementTypeStaticText[contains(@label, "Departures")]');
        await departuresTab.click();
        const departuresList = await client.$('//XCUIElementTypeStaticText[contains(@label, "Flight Number")]');
        if (await departuresList.isDisplayed()) {
            console.log('Departures list displayed.');
        } else {
            throw new Error('Departures list not displayed.');
        }
    } catch (error) {
        console.error('Error in testCase8:', error);
        throw error;
    }
}

async function testCase9(client) {
    try {
        // Verify the user can view arrival flights.
        const arrivalsTab = await client.$('//XCUIElementTypeStaticText[contains(@label, "Arrivals")]');
        await arrivalsTab.click();
        const arrivalsList = await client.$('//XCUIElementTypeStaticText[contains(@label, "Flight Number")]');
        if (await arrivalsList.isDisplayed()) {
            console.log('Arrivals list displayed.');
        } else {
            throw new Error('Arrivals list not displayed.');
        }
    } catch (error) {
        console.error('Error in testCase9:', error);
        throw error;
    }
}

async function testCase10(client) {
    try {
        // Verify the display of flight statuses in the departures list.
        const flightStatus = await client.$('//XCUIElementTypeStaticText[contains(@label, "Departing")]');
        if (await flightStatus.isDisplayed()) {
            console.log('Flight status displayed correctly.');
        } else {
            throw new Error('Flight status not displayed correctly.');
        }
    } catch (error) {
        console.error('Error in testCase10:', error);
        throw error;
    }
}

// Main function to run all test cases
(async () => {
    const client = await remote({
        logLevel: 'info',
        path: '/wd/hub',
        capabilities: {
            platformName: 'iOS',
            deviceName: 'iPhone Simulator',
            app: '/path/to/your/app.app',
            automationName: 'XCUITest',
        },
    });

    try {
        await testCase1(client);
        await testCase2(client);
        await testCase3(client);
        await testCase4(client);
        await testCase5(client);
        await testCase6(client);
        await testCase7(client);
        await testCase8(client);
        await testCase9(client);
        await testCase10(client);
    } catch (error) {
        console.error('Test execution failed:', error);
    } finally {
        await client.deleteSession();
    }
})();