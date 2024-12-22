# Electricity Billing System

This project is a comprehensive Electricity Billing System designed to calculate and manage electricity consumption data for various types of consumers. The system supports multiple consumer types such as industrial, residential, agricultural, and others. It calculates detailed billing components like electricity consumption fees, VAT, municipal taxes, and provides summaries for statistical analysis.

## Features

### Consumer Types:

Industrial, Residential, Agricultural, Public and Private, Lighting

### Billing Calculations:

Single-time and multi-time tariffs.

VAT and municipal tax calculations.

Profit/loss analysis based on tariff preferences.

### Consumer Insights:

Total electricity consumption.

Percentage distribution of consumers by type.

High-bill and high-consumption detection for industrial consumers.

### Statistical Summaries:

Average electricity consumption by consumer type.

Total revenue breakdown for the electricity company, municipality, and state.

User-Friendly Prompts:

Input validation to ensure data integrity.

Interactive questions to determine consumer eligibility for discounts or preferred tariffs.

## Usage

### Input Consumer Data:

Provide the consumer number and type.

Enter electricity consumption data for different time periods (daytime, peak, night).

Specify whether the consumer is eligible for discounts (e.g., veterans or families of martyrs).

### Select Tariff Preferences:

Choose between single-time and multi-time tariffs.

### View Results:

The system calculates and displays the total bill, electricity consumption fees, taxes, and profit/loss amounts.

### Statistics:

After processing all consumer data, the system outputs a summary of insights and statistics.

### Example Output

Your consumer no is: 1234
Your consumer type is: Residential
Your total electricity consumption amount in this period is: 450.00 kWh
Your total invoice amount for this period is: 1500.00 TL
Your profit/loss amount according to the other tariff is: -50.00 TL
Industry type number of consumers and their percentage is: 20, %10
...

### Project Structure

electricity_billing_system.py: The main script containing all logic and calculations.

README.md: Documentation for the project.

### Configuration

This system uses predefined constants for various fees and rates (e.g., VAT rates, electricity fees). You can adjust these constants in the script to match real-world scenarios or updated tariffs.

Future Enhancements

Integration with a database for storing consumer data.

GUI for improved user experience.

Web-based interface for remote access.

Inspired by real-world electricity billing systems.
