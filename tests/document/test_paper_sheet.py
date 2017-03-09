##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2016 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
from django.test.testcases import TestCase
from voluptuous import error as voluptuous_error

from osis_common.document import paper_sheet


class TestPaperSheet(TestCase):
    def test_valid_data(self):
        data = getRightData()
        self.assertEqual(data, paper_sheet.validate_data_structure(data))

    def test_data_empty(self):
        with self.assertRaises(voluptuous_error.MultipleInvalid):
            paper_sheet.validate_data_structure({})

    def test_data_with_wrong_link_to_regulation(self):
        data = getRightData()
        data['link_to_regulation']="testnotemail"

        try :
            paper_sheet.validate_data_structure(data)
            self.fail("The link to regulation must be a valid URL")
        except voluptuous_error.Invalid as e:
            self.assertIsInstance(e.errors[0], voluptuous_error.UrlInvalid)

    def test_data_with_no_learning_unit_years(self):
        data = getRightData()
        del data['learning_unit_years']

        try :
            paper_sheet.validate_data_structure(data)
            self.fail("The learning unit years is a mandatory field")
        except voluptuous_error.Invalid as e:
            self.assertIsInstance(e.errors[0], voluptuous_error.RequiredFieldInvalid)

    def test_data_with_bad_value_on_learning_unit_years(self):
        data = getRightData()
        data['learning_unit_years'] = "not list" #must be a list

        try :
            paper_sheet.validate_data_structure(data)
            self.fail("The learning unit years must be a list")
        except voluptuous_error.Invalid as e:
            self.assertIsInstance(e.errors[0], voluptuous_error.SequenceTypeInvalid)

    def test_data_with_session_number_not_integer(self):
        data = getRightData()
        data['learning_unit_years'][0]['session_number']="NOT INT"

        try :
            paper_sheet.validate_data_structure(data)
            self.fail("Session number must be an integer")
        except voluptuous_error.Invalid as e:
            self.assertIsInstance(e.errors[0], voluptuous_error.TypeInvalid)

    def test_data_with_decimal_scores_flag_not_bool(self):
        data = getRightData()
        data['learning_unit_years'][0]['decimal_scores'] = "NOT BOOL"

        try :
            paper_sheet.validate_data_structure(data)
            self.fail("Decimal scores allowed must be a bool")
        except voluptuous_error.Invalid as e:
            self.assertIsInstance(e.errors[0], voluptuous_error.TypeInvalid)

    def test_data_with_no_programs_key_in_learning_unit(self):
        data = getRightData()
        del data['learning_unit_years'][0]['programs']

        try :
            paper_sheet.validate_data_structure(data)
            self.fail("Programs key must exist in learning unit years")
        except voluptuous_error.Invalid as e:
            self.assertIsInstance(e.errors[0], voluptuous_error.RequiredFieldInvalid)

    def test_data_with_bad_value_on_programs(self):
        data = getRightData()
        data['learning_unit_years'][0]['programs'] = "not list"  # must be a list

        try:
            paper_sheet.validate_data_structure(data)
            self.fail("Programs key in learning unit years must be a list")
        except voluptuous_error.Invalid as e:
            self.assertIsInstance(e.errors[0], voluptuous_error.SequenceTypeInvalid)

    def test_data_with_no_enrollement_key_in_learning_unit(self):
        data = getRightData()
        del data['learning_unit_years'][0]['programs'][0]['enrollments']

        try :
            paper_sheet.validate_data_structure(data)
            self.fail("Enrollement key must exist in learning unit years - programs")
        except voluptuous_error.Invalid as e:
            self.assertIsInstance(e.errors[0], voluptuous_error.RequiredFieldInvalid)

    def test_data_with_bad_value_on_enrollement_key_in_learning_unit(self):
        data = getRightData()
        data['learning_unit_years'][0]['programs'][0]['enrollments'] = "bad value"

        try:
            paper_sheet.validate_data_structure(data)
            self.fail("Enrollement key must be a list in learning unit years - programs")
        except voluptuous_error.Invalid as e:
            self.assertIsInstance(e.errors[0], voluptuous_error.SequenceTypeInvalid)

    def test_check_pdf_generation(self):
        data = getRightData()
        http_response = paper_sheet.build_response(data)
        self.assertEqual(http_response.status_code, 200)
        self.assertIsNotNone(http_response.content)
        self.assertEqual(http_response['content-type'], 'application/pdf')


def getRightData() :
    #Return a valid template data
    return {
        'institution': 'Université catholique de Louvain',
        'link_to_regulation': 'https://www.uclouvain.be/enseignement-reglements.html',
        'publication_date': '2/3/2017',
        'justification_legend': "Légende pour le champ 'Justification': A=Absent, T=Tricherie, ?=Note manquante",
        'tutor_global_id': '',
        'learning_unit_years': [{
            'session_number': 1,
            'coordinator': {
                'address': {
                    'city': 'Louvain-la-Neuve',
                    'postal_code': '1348',
                    'location': "Traverse d'Esope 1 bte L1.07.01"
                },
                'first_name': 'Anne-Julie',
                'last_name': 'Toubeau'
            },
            'programs': [{
                'deadline': '',
                'deliberation_date': 'Non communiquée',
                'acronym': 'CHIM1BA',
                'address': {
                    'city': 'Louvain-la-Neuve',
                    'fax': '010472837',
                    'postal_code': '1348',
                    'recipient': 'SC',
                    'phone': '010473324',
                    'email': 'emil_fac_chim1ba@uclouvain.be',
                    'location': 'Place des Sciences, 2L6.06.01'
                },
                'enrollments': [{
                    'registration_id': '36661500',
                    'first_name': 'Géraldine',
                    'last_name': 'Chanteux',
                    'justification': '',
                    'score': '14'
                }, {
                    'registration_id': '17151400',
                    'first_name': 'Jordan',
                    'last_name': 'Crutzen',
                    'justification': 'Tricherie',
                    'score': ''
                }, {
                    'registration_id': '11661500',
                    'first_name': 'Emmerance',
                    'last_name': 'Gillon',
                    'justification': 'Tricherie',
                    'score': ''
                }, {
                    'registration_id': '37641300',
                    'first_name': 'Sharon',
                    'last_name': 'Hubert',
                    'justification': 'Tricherie',
                    'score': ''
                }, {
                    'registration_id': '04501500',
                    'first_name': 'Corentin',
                    'last_name': 'Pochet',
                    'justification': 'Tricherie',
                    'score': ''
                }, {
                    'registration_id': '02771400',
                    'first_name': 'Maria',
                    'last_name': 'Shoueiry',
                    'justification': 'Note manquante',
                    'score': ''
                }]
            }],
            'title': 'English: reading and listening comprehension of scientific texts - C',
            'academic_year': '2016-2017',
            'acronym': 'LANG1862C',
            'decimal_scores': False
        }]
    }