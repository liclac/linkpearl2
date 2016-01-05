import { moduleForModel, test } from 'ember-qunit';

moduleForModel('grand-company', 'Unit | Serializer | grand company', {
  // Specify the other units that are required for this test.
  needs: ['serializer:grand-company']
});

// Replace this with your real tests.
test('it serializes records', function(assert) {
  let record = this.subject();

  let serializedRecord = record.serialize();

  assert.ok(serializedRecord);
});
