// Sample data for categories and values
const mainCategory = 'Colleges';
const categories = ['Engineering', 'Liberal Arts', 'Science', 'COBA', 'Education'];
const values = [4, 3, 2, 5, 4]; // Example data, replace with your own

// Set up dimensions for the spider diagram
const diagramWidth = 600; // Set the desired width of the diagram
const diagramHeight = 600; // Set the desired height of the diagram
const margin = { top: 50, right: 50, bottom: 50, left: 50 };

// Create SVG element
const svg = d3.select('#spider-diagram')
    .append('svg')
    .attr('width', diagramWidth)
    .attr('height', diagramHeight);

// Calculate the maximum text width
const maxTextWidth = Math.max(...categories.map(d => getTextWidth(d)));

// Draw lines from main category to subcategories
const mainCategoryX = diagramWidth / 2;
const mainCategoryY = diagramHeight / 2;
svg.selectAll('.main-line')
    .data(categories)
    .enter()
    .append('line')
    .attr('class', 'main-line')
    .attr('x1', mainCategoryX)
    .attr('y1', mainCategoryY)
    .attr('x2', (d, i) => Math.cos(i * Math.PI * 2 / categories.length) * (maxTextWidth * 3) + diagramWidth / 2) // Adjust the multiplier to increase distance
    .attr('y2', (d, i) => Math.sin(i * Math.PI * 2 / categories.length) * (maxTextWidth * 3) + diagramHeight / 2) // Adjust the multiplier to increase distance
    .attr('stroke', 'gray');

// Draw circles for subcategories
svg.selectAll('.subcircle')
    .data(categories)
    .enter()
    .append('circle')
    .attr('class', 'subcircle')
    .attr('cx', (d, i) => Math.cos(i * Math.PI * 2 / categories.length) * (maxTextWidth * 3) + diagramWidth / 2) // Adjust the multiplier to increase distance
    .attr('cy', (d, i) => Math.sin(i * Math.PI * 2 / categories.length) * (maxTextWidth * 3) + diagramHeight / 2) // Adjust the multiplier to increase distance
    .attr('r', maxTextWidth / 2 + 5) // Set the circle radius based on the maximum text width
    .attr('fill', 'blue')
    .on('click', function (event, d) {
        // Handle the click event
        d3.select(this)
            .transition()
            .duration(500) // Animation duration in milliseconds
            .attr('r', maxTextWidth / 2 + 10) // Increase circle size
            .transition()
            .duration(500) // Animation duration in milliseconds
            .attr('r', maxTextWidth / 2 + 5); // Restore circle size after animation
    });

// Add text labels inside circles for subcategories
svg.selectAll('.subcircle-label')
    .data(categories)
    .enter()
    .append('text')
    .attr('class', 'subcircle-label')
    .attr('x', (d, i) => Math.cos(i * Math.PI * 2 / categories.length) * (maxTextWidth * 3) + diagramWidth / 2) // Adjust the multiplier to increase distance
    .attr('y', (d, i) => Math.sin(i * Math.PI * 2 / categories.length) * (maxTextWidth * 3) + diagramHeight / 2 + 5) // Adjust the multiplier to increase distance
    .attr('text-anchor', 'middle')
    .attr('dominant-baseline', 'middle')
    .text(d => d)
    .attr('fill', 'white');

// Display main category in the middle
svg.append('text')
    .attr('x', mainCategoryX)
    .attr('y', mainCategoryY)
    .attr('text-anchor', 'middle')
    .attr('dominant-baseline', 'middle')
    .text(mainCategory)
    .attr('fill', 'black');

// Function to calculate the width of the text
function getTextWidth(text) {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    context.font = '14px sans-serif'; // Set the font style and size
    return context.measureText(text).width;
}