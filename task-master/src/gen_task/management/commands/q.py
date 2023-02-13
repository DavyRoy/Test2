import random

from django.core.management.base import BaseCommand

from datetime import timedelta

from django.utils import timezone

from gen_task.models import Task, CheckPoint, CommentTask, TaskFile, SubTask
from gen_task.tests.fixtures_factory import CheckPointFactory, TaskFactory, CommentTaskFactory, TaskFileFactory, SubTaskFactory


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        ids = ['9df7892f-2cd8-47a9-92b3-efad25cf70d5', '4b057de0-8842-4b7b-81c8-56c568a79046',
               '369cc06f-e117-4d81-8c7a-60615b80e7ca', '418956a0-ebfe-4924-b4fd-4a0cba7a3fc2',
               'bdaec4be-6bb9-4c98-917f-21187da6b7de', '450dc1b1-7ee2-4b4a-b0f6-d430338d294f',
               'ae9b858e-3869-48ab-958c-949e52efd2d6', '73e3ce3c-acb3-45a0-b1a1-5639359bea2d',
               '4414ba1d-8b67-498b-91da-7574a20bf6cf', '8da19772-4ed5-405b-b92b-77749d4c8fd9',
               'cfe8a6e8-587a-4e35-934c-db438677a418', 'a0c10ad4-5287-4a13-a622-456da8229456',
               '10ebb060-b43e-404e-965b-93b7dfdbf469', '00fc311d-fccf-4d31-9e2a-9fbe1be6d748',
               '93e48798-8af9-4af8-982e-5ada159535ab', 'cf88928d-8631-41a6-8dc8-d04c4422a417',
               '25928f02-9bc9-49f2-bd10-d5b465206e54', '635cfc05-9411-43b2-aa52-6e81e3e83c91',
               '92a8b115-0052-4920-90e8-7c7273ce0fc5', 'dc8e1ad8-aa42-4ec0-bfd7-7fea5b38b33c',
               '4e844376-f2a3-4fba-ad8d-8a25db07dd09', 'd37a8ec5-6ed5-40bf-9111-39ad21e123ba',
               'be5b6e87-c546-445e-bcc5-966ffe20eae2', '07199e73-c18a-4460-a2fb-9f68af2972aa',
               '315bb9de-f658-44e0-a1bd-8677e54cb926', 'c34dd23e-717f-4432-a66d-f2d81250a5f4',
               '3b7a3ad2-b612-4b30-bfc5-bf8e438fbbfe', 'd901f6f8-e108-4262-b674-00f4ca602ab8',
               '8357d9be-0a08-4d03-905b-b3ebd0262c64', 'a88e61e3-c50a-4b57-b1b8-3cd3ba923595',
               '63d5fb29-0db0-4f38-83bb-54a9b18dbe12', 'd4df7c7b-7d43-4dba-afc8-b3f2f5d50644',
               '1075afd1-e447-4f41-88eb-94d3e33cc250', 'bf5ed3ed-7c3b-4514-b7a7-41a3a8948aa0',
               '23955a6b-ba25-47f1-96e6-f2a0ebd71979', '1b480238-6bc4-4600-8a1a-bcc98e0213fe',
               '417a7684-5ca8-469e-8bad-4b00341e960a', '264ebe5b-c01d-4d08-9d0f-bddec99077b3',
               'dff42de9-dc11-4823-a204-df03c018d528', '583fb678-b25e-491d-bc41-398cda8d6cbf',
               '63902288-5153-4768-96fa-370a941b7d15', '69bc75d0-3af8-4bdb-94bb-c139dd39c18d',
               '2f5f33ec-eb73-404d-82cd-0f55be51dc2b', 'ef817888-a143-4699-8ba3-b7bb859039ab',
               '6dc5df70-0982-4c5e-b48b-e4b3994df96f', 'f6041df4-4961-48cc-a21c-a88e18f32abb',
               '8d38988d-f26c-4a8d-b2bc-6ec96a566562', '1055267a-b2e1-4663-a5fd-99879e52ac3a',
               '9f253342-47ad-468d-8fda-34276225196a', 'ed93dee5-08ba-477a-947d-b73e5d09dc76',
               'b4db8003-6bd1-49bb-a51e-82320e6dd940', 'c051a28f-1629-4f64-bd4b-ce67ee503d38',
               '3875abcb-a7a4-4ad8-a222-705ad1fb836c', '049e70cc-0b54-4de9-8323-72c7e90ee45b',
               '5220bfb5-5a33-4068-b3c1-7010a974c494', 'edfaa13e-156a-47ce-9d65-eb13be1bb048',
               '57989e0c-f691-46c0-92ff-a8da6a5b875a', 'fa74b780-4728-46f3-acce-df2d26ae99e4',
               '819e770b-1a9a-43a2-b3b0-779dd8b2b569', '598ae370-584e-4ce6-b35c-e344990b2be6',
               '67117e7a-0344-4f01-a73d-e146884a9877', '84b16e15-d15c-4179-919b-262c7c8fdafe',
               'b156a0c3-c2fb-473b-8832-39b5f504bbcd', 'de270ac8-df92-4eea-b7a2-0eea19c7fb16',
               '611925b0-3fcb-42a5-8ac0-257c6672a38a', '6e31cd3e-4066-4498-86f4-76b59ac817a5',
               'a345f5f9-9a36-4ab8-a8da-0643c8f113df', 'ca345233-320d-4617-99fd-687c65aecab7',
               '739cfcc5-3c2a-4bf8-9e7a-84b796f3edbe', 'a8142bae-bb6b-4799-ac35-4e7184e2906b',
               '893bbac8-d548-45a2-bc97-d6fd81131a80', 'b8cfdac1-6f5e-44b0-a03b-b53e1e46608c',
               '5805aec2-143a-4b35-8b5b-f32ac6acec4f', '43b54721-5480-493a-aad7-ea1a7be2ff5f',
               'f1faa402-3446-4b5c-bed6-9f04799943b2', 'b68e4bab-d5fd-4291-a27b-35d1b40c94f7',
               '361ca139-6a4b-4908-aab1-a31ec9e94757', 'caa91865-7035-49d3-b8d6-bed5c5dbcaa2',
               'e1883c2e-93f4-4f5d-9c9f-51691af8d908', 'c034f4f6-ce8a-4c30-8c66-2886904298c1',
               '8ba207a6-fae0-4f4f-aad1-06077d398444', 'ca85f7a6-f7b1-4d0c-93f9-3817786d6503',
               '62123cfc-c1ab-4398-bc11-24d411ee9a71', '64eb1a8a-6bd8-426a-b1e6-06a0d32fa8d7',
               '6bdd53ed-d403-4a3a-9a53-40a1e4549ce0', '7202ed2d-37d8-4c35-a317-47038753984c',
               '76d92b20-6e89-4461-bca8-533d6dacfae0', 'c68b0d53-b19b-4dfd-8a7e-6d816e59d428',
               '9c3ac5d3-53fa-43ef-aaca-06bfb0612b94', '797ee332-e80b-4a79-96f6-18b9d5cf11e4',
               'afe1db64-fb0f-4a1d-a818-b574d6da1c61', '9ef9fb87-a9ed-4750-a34f-ba730e3231c2',
               'cc7563ba-db9e-42cc-afa6-4b27a1943172', '6d1f98bd-eb67-4a43-9b57-abc14eacce23',
               'df54ff37-b861-42b6-9152-27524e3c871e', '8a54d660-bb73-4ebd-8dd0-9fde2a502225',
               'b2f7c250-aa8f-4e93-b401-a48b57577f29', 'cfffd69e-6960-4c57-8a43-2a46f8183c08',
               'f1aa1e62-c5be-478b-ac07-fbf7f7a4470e', '57d7dca5-cd70-480f-8744-377a1c753459',
               'a9e77a1b-774c-495b-bce3-91943bfeb425', 'a4345173-d4e2-40c9-88df-19b0d36c9bb5',
               'd5aca689-1dc7-49d0-a8de-cdb3f89c2228', 'ba2cd20d-eb4d-4d8e-bfb9-a84762f5c838']

        for _ in range(50):
            task = TaskFactory.create(
                executor=random.choice(ids),
                updated_by=random.choice(ids),
                created_by=random.choice(ids),
                reviewers=[random.choice(ids) for _ in range(random.randint(0, 6))],
                observers=[random.choice(ids) for _ in range(random.randint(0, 6))],
                responsible=[random.choice(ids) for _ in range(random.randint(0, 6))],
                check_point=None,
                previous_task=None,
                started_at=timezone.now() + timedelta(days=30),
                planned_ended_at=timezone.now() + timedelta(days=60)
            )

            CommentTaskFactory.create(
                updated_by=random.choice(ids),
                created_by=random.choice(ids),
                task=task
            )
            TaskFileFactory.create(
                updated_by=random.choice(ids),
                created_by=random.choice(ids),
                task=task
            )
            SubTaskFactory.create(
                updated_by=random.choice(ids),
                created_by=random.choice(ids),
                task=task
            )

