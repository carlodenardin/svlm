// --- 1. IMPOSTAZIONI DEL GRAFICO ---
const margin = {top: 20, right: 30, bottom: 40, left: 50};
const width = 960 - margin.left - margin.right;
const height = 500 - margin.top - margin.bottom;

// Aggiungiamo l'elemento SVG al div #grafico
const svg = d3.select("#grafico")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

// --- 2. CARICAMENTO E PREPARAZIONE DEI DATI ---
d3.csv("dati.csv").then(function(data) {

    // Convertiamo le stringhe numeriche in numeri
    data.forEach(d => {
        d.rateo_successo = +d.rateo_successo; // Il '+' converte in numero
    });
    
    // Salviamo una copia dei dati completi
    const datiCompleti = data;

    // --- 3. POPOLIAMO I FILTRI DINAMICAMENTE ---
    
    // Estraiamo i valori unici per 'diagramma' e 'livello'
    const tuttiDiagrammi = ["Tutti", ...new Set(data.map(d => d.diagramma))];
    const tuttiLivelli = ["Tutti", ...new Set(data.map(d => d.livello))];

    // Popoliamo il primo menu a tendina
    d3.select("#filtro-diagramma")
      .selectAll('option')
      .data(tuttiDiagrammi)
      .enter()
      .append('option')
      .text(d => d)
      .attr("value", d => d);

    // Popoliamo il secondo menu a tendina
    d3.select("#filtro-livello")
      .selectAll('option')
      .data(tuttiLivelli)
      .enter()
      .append('option')
      .text(d => d)
      .attr("value", d => d);
    
    // --- 4. DEFINIAMO LE SCALE E GLI ASSI ---
    
    // Asse X (per i problemi)
    const x = d3.scaleBand()
        .range([0, width])
        .padding(0.1);
    
    // Asse Y (per il rateo successo)
    const y = d3.scaleLinear()
        .domain([0, 1]) // Rateo va da 0 a 1
        .range([height, 0]);
    
    // Scala dei colori (per i modelli)
    const colore = d3.scaleOrdinal(d3.schemeCategory10);

    const asseX = svg.append("g")
        .attr("transform", `translate(0,${height})`);
        
    const asseY = svg.append("g");

    // --- 5. LA FUNZIONE DI AGGIORNAMENTO ⚙️ ---
    // Questa funzione viene chiamata ogni volta che si disegna o si aggiorna il grafico
    function update(datiFiltrati) {
        
        // Aggiorniamo i domini delle scale
        x.domain(datiFiltrati.map(d => d.problema));
        colore.domain([...new Set(datiFiltrati.map(d => d.modello))]);

        // Aggiorniamo gli assi
        asseX.call(d3.axisBottom(x));
        asseY.call(d3.axisLeft(y));

        // Data Join per i punti (cerchi)
        const punti = svg.selectAll("circle")
            .data(datiFiltrati);
        
        punti.join(
            // ENTER: crea i nuovi punti
            enter => enter.append("circle")
                .attr("cx", d => x(d.problema) + x.bandwidth() / 2)
                .attr("cy", d => y(d.rateo_successo))
                .attr("r", 7)
                .style("fill", d => colore(d.modello))
                .style("opacity", 0.7),
            // UPDATE: aggiorna i punti esistenti (per transizioni)
            update => update
                .attr("cx", d => x(d.problema) + x.bandwidth() / 2)
                .attr("cy", d => y(d.rateo_successo)),
            // EXIT: rimuove i punti che non servono più
            exit => exit.remove()
        );
    }

    // --- 6. GESTIAMO GLI EVENTI DEI FILTRI ---
    
    function onFilterChange() {
        const diagrammaSelezionato = d3.select("#filtro-diagramma").property("value");
        const livelloSelezionato = d3.select("#filtro-livello").property("value");

        // Filtriamo i dati in base alle selezioni
        let datiFiltrati = datiCompleti.filter(d => {
            const matchDiagramma = (diagrammaSelezionato === "Tutti" || d.diagramma === diagrammaSelezionato);
            const matchLivello = (livelloSelezionato === "Tutti" || d.livello === livelloSelezionato);
            return matchDiagramma && matchLivello;
        });
        
        // Chiamiamo la funzione di aggiornamento con i nuovi dati
        update(datiFiltrati);
    }
    
    d3.select("#filtro-diagramma").on("change", onFilterChange);
    d3.select("#filtro-livello").on("change", onFilterChange);

    // --- 7. DISEGNAMO IL GRAFICO INIZIALE ---
    update(datiCompleti);

});