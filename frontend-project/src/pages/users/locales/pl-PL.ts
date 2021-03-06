export const usersLocale = {
  users: {
    fields: {
      username: 'Nazwa użytkownika',
      password: 'Hasło',
      email: 'Email',
      firstName: 'Imię',
      lastName: 'Nazwisko',
    },
    list: {
      pageHeaderContent: 'Lista użytkowników',
      table: {
        header: 'Lista użytkowników',
      },
    },
    detailView: {
      newPageHeaderContent: 'Tworzenie użytkownika',
      editPageHeaderContent: 'Edytowanie użytkownika',
      placeholders: {
        username: 'Nazwa użytkownika',
        password: 'Długie i bezpieczne hasło',
        email: 'contact@sample.com',
        firstName: 'Imię',
        lastName: 'Nazwisko',
      },
      errors: {
        username: 'Nazwa użytkownika jest wymagana',
        password: 'Hasło jest wymagane',
        email: 'Email jest wymagany',
      },
    },
    errors: {
      fetchFailed: 'Nie udało się pobrać użytkowników',
      removeFailed: 'Nie udało się usunąć użytkownika.',
      updateFailed: 'Edycja użytkownika nie powiodła się.',
      createFailed: 'Utworzenie użytkownika nie powiodło się.',
      authFailed: 'Nie udało się zalogować użytkownika.',
      refreshFailes: 'Nie udało się odświeżyć tokenu.',
    },
  },
};
