#!/usr/bin/python3
	
zones2020 = {
	'Zone C' : ('Afghanistan', 'Angola', 'Bangladesh', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Côte d\'Ivoire', 'Djibouti', 'Dominica', 'El Salvador', 'Eritrea', 'Ethiopia', 'Gambia', 'Ghana', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'India', 'Jamaica', 'Jordan', 'Kenya', 'Kiribati', 'Kyrgyzstan', 'Laos', 'Lesotho', 'Liberia', 'Madagascar', 'Malawi', 'Mali', 'Marshall Islands', 'Mauritania', 'Micronesia', 'Moldova', 'Morocco', 'Mozambique', 'Myanmar', 'Nepal', 'Nicaragua', 'Niger', 'Nigeria', 'Pakistan', 'Papua New Guinea', 'Philippines', 'Rwanda', 'Samoa', 'Senegal', 'Sierra Leone', 'Solomon Islands', 'South Sudan', 'Sudan', 'Tajikistan', 'Tanzania', 'Timor-Leste', 'Togo', 'Tonga', 'Tuvalu', 'Uganda', 'Uzbekistan', 'Vanuatu', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'),
	'Zone D' : ('Albania','Ukraine', 'Algeria', 'Armenia', 'Azerbaijan', 'Barbados', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'China', 'Colombia', 'Costa Rica', 'Dominican Republic', 'Ecuador', 'Egypt', 'Eswatini', 'Fiji', 'Gabon', 'Georgia', 'Grenada', 'Indonesia', 'Iran', 'Iraq', 'Kosovo', 'Lebanon', 'Libya', 'Mongolia', 'Montenegro', 'Namibia', 'Nauru', 'Macedonia', 'Palau', 'Paraguay', 'Peru', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Serbia', 'South Africa', 'Sri Lanka', 'Suriname', 'Thailand', 'Tunisia', 'Turkmenistan'),
	'Zone E' : ('Antigua and Barbuda', 'Argentina', 'Belarus', 'Bulgaria', 'Chile', 'Croatia', 'Equatorial Guinea', 'Greece', 'Kazakhstan', 'Latvia', 'Maldives', 'Mauritius', 'Mexico', 'Panama', 'Romania', 'Russia', 'Saint Kitts and Nevis', 'Turkey', 'Uruguay'),
	'Zone F' : ('Bahamas', 'Cyprus', 'Czech Republic', 'Estonia', 'Hungary', 'Israel', 'Italy', 'Lithuania', 'Malaysia', 'Poland', 'Portugal', 'Puerto Rico', 'Seychelles', 'Slovakia', 'Slovenia', 'Trinidad and Tobago'),
	'Zone G' : ('G','Belgium', 'Canada', 'Finland', 'France', 'Japan', 'South Korea', 'Malta', 'New Zealand', 'Oman', 'Spain', 'United Kingdom'),
	'Zone H' : ('H','Australia', 'Austria', 'Bahrain', 'Denmark', 'Germany', 'Iceland', 'Netherlands', 'Saudi Arabia', 'Sweden', 'Taiwan'),
	'Zone I' : ('I','Switzerland', 'Brunei', 'Hong Kong', 'Ireland', 'Kuwait', 'Luxembourg', 'Macau', 'Norway', 'Qatar', 'San Marino', 'Singapore', 'United Arab Emirates', 'United States')

}

errorMessage = 'None'

def find_zone(country):
	for i in zones2020:
		if country in zones2020[i]:
			return(i)
	else:
		return(errorMessage)

# print(find_zone(input('Please enter a country:\n  ')))
