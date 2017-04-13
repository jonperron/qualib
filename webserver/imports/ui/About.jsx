import React, { Component, PropTypes } from 'react';

export default class About extends Component {
	render() {
		return (
			<div className="aboutQualib">
				<br />
				<br />
				<h4>"Mon train sera-t-il à l'heure aujourd'hui ?"</h4>
				<p>Quali'B est un projet open-source visant à répondre à cette fameuse question que chaque usager de train s'est posé un jour.<br/>
				La différence par rapport aux autres services disponible en ligne ? Des horaires prédictifs fournis à l'aide de données réelles, et capable de prendre en compte
				des perturbations (retards, accidents, etc.)</p>
				<br />
				<p>Quali'B est développé spécifiquement pour le RER B pour lequel les informations sont très peu nombreuses. Il sera peut-être étendu à d'autres lignes ferroviaires
				dans le futur, s'il se montre fiable :-)</p>
				<br />
				<p> Le projet a trois volets complémentaires :
					<ul>
						<li>Une description qualitative de la qualité du trafic du RER B;</li>
						<li>Une description quantitative de cette même qualité;</li>
						<li>Une description prédictive lors de la recherche d'horaires qui s'adapteront au mieux aux conditions réelles de transport</li>
					</ul>
				</p>
				<br />
				<p>Quali'B tire ses informations des sources suivantes:
					<ul>
						<li>L'API Temps Réel de la RATP : <a href="https://data.ratp.fr/page/temps-reel/" target="_blank">https://data.ratp.fr/page/temps-reel/</a>;</li>
						<li>L'API Temps Réel Transilien de la SNCF : <a href="https://ressources.data.sncf.com/explore/dataset/api-temps-reel-transilien/" target="_blank">https://ressources.data.sncf.com/explore/dataset/api-temps-reel-transilien/</a>;</li>
						<li>Open Data SNCF : <a href="https://ressources.data.sncf.com/explore/?sort=modified" target="_blank">https://ressources.data.sncf.com/explore/?sort=modified</a>.</li>
					</ul>
				</p>
				<br />
				<p>Historique des versions :
					<table className="table">
						<tbody>
							<tr>
								<td>Avril 2017</td>
								<td>Alpha</td>
								<td>Alpha technique de Quali'B</td>
							</tr>
						</tbody>
					</table>
				</p>
			</div>
		)
	}
}